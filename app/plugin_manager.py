import importlib.util
import os
import pkgutil
from app.plugins.plugin import Plugin  

class PluginManager:
    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir
        self.plugins = {}

    def load_plugins(self):
        plugin_dir_str = str(self.plugin_dir)
        print(f"Loading plugins from: {plugin_dir_str}")

        for _, module_name, is_pkg in pkgutil.iter_modules([plugin_dir_str]):
            if module_name == "bad_plugin":
                print("Skipping bad_plugin.")
                continue
            
            try:
                
                spec = importlib.util.spec_from_file_location(module_name, os.path.join(plugin_dir_str, f"{module_name}.py"))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

              
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if isinstance(attr, type) and issubclass(attr, Plugin) and attr is not Plugin:
                        plugin_instance = attr()  
                        self.plugins[module_name] = plugin_instance
                        print(f"Loaded plugin: {module_name}")
                        break
                else:
                    print(f"No valid plugin class found in {module_name}.")
            except ImportError as e:
                print(f"Failed to load plugin {module_name}: {e}")
            except Exception as e:
                print(f"An error occurred while loading plugin {module_name}: {e}")

        print(f"Loaded plugins: {list(self.plugins.keys())}")

    def run_plugins(self):
        for name, plugin in self.plugins.items():
            print(f"Running plugin: {name}")
            if hasattr(plugin, 'run'):
                plugin.run()
            else:
                print(f"Plugin {name} does not have a run method.")
