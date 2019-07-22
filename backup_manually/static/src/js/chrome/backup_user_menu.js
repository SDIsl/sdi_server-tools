odoo.define('backup_manually.UserMenu', function (require) {
    "use strict";

    var UserMenu = require('web.UserMenu');

    UserMenu.include({
    _onMenuBackup: function () {
        var self = this;
        this.trigger_up('clear_uncommitted_changes', {
            callback: function () {
                self._rpc({
                        route: "/web/action/load",
                        params: {
                            action_id: "backup_manually.backup_manually_action",
                        },
                    })
                    .done(function (result) {
                        self.do_action(result);
                    });
            },
        });
    },
    })
})
