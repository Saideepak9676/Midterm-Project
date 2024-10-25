from unittest.mock import patch
import pytest
from app.plugin_manager import PluginManager
from app.plugins.greet.greet_plugins import GreetPlugin  # Ensure GreetPlugin has a `run` method that prints a message
from app.plugins.plugin import Plugin  # Abstract Plugin class

# Test NotImplementedError raised by Plugin
def test_plugin_run_not_implemented():
    with pytest.raises(TypeError) as excinfo:
        Plugin()  # Abstract Plugin instantiation should raise an error
    assert "Can't instantiate abstract class Plugin" in str(excinfo.value)

# Test the functionality of the GreetPlugin's run method
def test_greet_plugin_run():
    plugin = GreetPlugin()  # Use concrete plugin class

    with patch("builtins.print") as mock_print:
        plugin.run()
        mock_print.assert_called_once_with(
            "Hello, welcome to the Advanced Python Calculator!"
        )

@pytest.fixture
def setup_plugins(tmp_path):
    plugins_dir = tmp_path / "plugins"
    plugins_dir.mkdir()

    # Valid plugin definition
    valid_plugin = plugins_dir / "valid_plugin.py"
    valid_plugin.write_text(
        """
from app.plugins.plugin import Plugin

class ValidPlugin(Plugin):
    def run(self):
        print("Hello from valid plugin!")
"""
    )

    # Invalid plugin definition
    bad_plugin = plugins_dir / "bad_plugin.py"
    bad_plugin.write_text(
        """
# Invalid plugin without a class or run method
"""
    )

    return str(plugins_dir)

# Test loading of plugins in PluginManager
def test_load_plugins(setup_plugins):
    plugin_manager = PluginManager(setup_plugins)
    plugin_manager.load_plugins()
    
    assert len(plugin_manager.plugins) == 1
    assert "valid_plugin" in plugin_manager.plugins
    assert isinstance(plugin_manager.plugins["valid_plugin"], Plugin)

# Test execution of loaded plugins
def test_run_plugins(setup_plugins):
    plugin_manager = PluginManager(setup_plugins)
    plugin_manager.load_plugins()
    
    with patch("builtins.print") as mock_print:
        plugin_manager.run_plugins()
        mock_print.assert_any_call("Hello from valid plugin!")

# Test that invalid plugins are skipped
def test_bad_plugin_handling(setup_plugins):
    plugin_manager = PluginManager(setup_plugins)
    plugin_manager.load_plugins()
    
    assert len(plugin_manager.plugins) == 1  # Only valid plugin should be loaded
    assert "valid_plugin" in plugin_manager.plugins
    assert "bad_plugin" not in plugin_manager.plugins
