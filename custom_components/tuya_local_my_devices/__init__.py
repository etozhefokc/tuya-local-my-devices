"""Tuya Local — My Devices.

Copies bundled device YAML configs into the tuya_local component's devices/
directory on Home Assistant startup, so they are picked up automatically.
"""
import logging
import shutil
from pathlib import Path

from homeassistant.core import HomeAssistant
from homeassistant.helpers.event import async_call_later

_LOGGER = logging.getLogger(__name__)
DOMAIN = "tuya_local_my_devices"


def _copy_device_files(source_dir: Path, dest_dir: Path) -> None:
    """Copy all YAML device files from source to destination."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    for yaml_file in source_dir.glob("*.yaml"):
        shutil.copy2(yaml_file, dest_dir / yaml_file.name)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Copy device YAMLs into tuya_local/devices/ at startup."""
    source = Path(__file__).parent / "devices"
    dest = Path(hass.config.config_dir) / "custom_components" / "tuya_local" / "devices"

    def _do_copy(*_):
        _copy_device_files(source, dest)
        _LOGGER.info("Copied Tuya Local device configs to %s", dest)

    # Delay slightly so tuya_local is already loaded
    async_call_later(hass, 1, _do_copy)
    return True
