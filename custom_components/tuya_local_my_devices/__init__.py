"""Tuya Local — My Devices.

Copies bundled device YAML configs into the tuya_local component's devices/
directory on Home Assistant startup, so they are picked up automatically.
"""
import logging
import shutil
from pathlib import Path

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.event import async_call_later

_LOGGER = logging.getLogger(__name__)
DOMAIN = "tuya_local_my_devices"


def _copy_device_files(source_dir: Path, dest_dir: Path) -> None:
    """Copy all YAML device files from source to destination."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    for yaml_file in source_dir.glob("*.yaml"):
        shutil.copy2(yaml_file, dest_dir / yaml_file.name)


def _do_copy(hass: HomeAssistant) -> None:
    """Copy device configs into tuya_local/devices/."""
    source = Path(__file__).parent / "devices"
    dest = Path(hass.config.config_dir) / "custom_components" / "tuya_local" / "devices"
    _copy_device_files(source, dest)
    _LOGGER.info("Copied Tuya Local device configs to %s", dest)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up via configuration.yaml — copy files then return."""
    async_call_later(hass, 1, lambda _: _do_copy(hass))
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up via UI config flow — copy files, set up platforms."""
    await hass.async_add_executor_job(_do_copy, hass)
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload — remove sensor platform."""
    return await hass.config_entries.async_unload_platforms(entry, ["sensor"])
