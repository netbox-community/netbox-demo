# NetBox Demo Plugin

**WARNING:** This plugin is purposefully insecure. Do not install it.

This plugin serves to ease the administration of the public NetBox demo instance at <https://demo.netbox.dev>. It performs the following tasks:

* Facilitate the automatic creation of new superuser accounts
* Prevent manipulation or deletion of the default admin user

## Change Log

### v0.4

* Implement the automatic creation of unique user accounts

### v0.3

* Protect against changes to the admin user's name, password, or status

### v0.2

* Separate `pre_save` and `pre_delete` signal handlers

### v0.1

* Initial release
