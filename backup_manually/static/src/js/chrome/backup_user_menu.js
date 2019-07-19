odoo.define('backup_manually.UserMenu', function (require) {
    "use strict";

    var Widget = require('web.Widget');
    var SystrayMenu = require('web.SystrayMenu');
    var UserMenu = require('web.UserMenu');
    var session = require('web.session');
    var Dialog = require('web.Dialog');
    var core = require('web.core');
    var ajax = require('web.ajax');
    var qweb = core.qweb;
    var _t = core._t;

    UserMenu.include({
    _onMenuBackup: function () {
        var self = this;
        var session = this.getSession();
        this.trigger_up('clear_uncommitted_changes', {
            callback: function () {
                self._rpc({
                        route: "/web/action/load",
                        params: {
                            action_id: "backup_manually.backup_manually_action",
                        },
                    })
                    .done(function (result) {
                        result.res_id = session.uid;
                        self.do_action(result);
                    });
            },
        });
    },
    })

})
