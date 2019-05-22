
.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

SDi-Tools: Update Geonames
=====================

Tool module for Zip_location updater using the zip field in the partner record.

Configuration
=============

Create a new Planned Action for res.partner 
of type python with the following code:

```python
model.search([]).update_geonames()
```

Usage
=====

Run Manually the new planned action.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/sale-workflow/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.


Credits
=======

Contributors
------------

* `SDI <http://www.sdi.es>`_

  * Oscar Soto <osoto@sdi.es>

Do not contact contributors directly about support or help with technical issues.
