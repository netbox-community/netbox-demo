from extras.plugins import PluginConfig


class NetBoxDemoConfig(PluginConfig):
    name = 'netbox_demo'
    verbose_name = 'Demo'
    description = 'Demo maintenance plugin'
    version = '0.3.1'
    base_url = 'demo'
    default_settings = {
        'admin_username': 'admin',
    }

    def ready(self):
        import netbox_demo.signals


config = NetBoxDemoConfig
