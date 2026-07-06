"""Sensor platform — shows count of device YAML files."""
from __future__ import annotations

import logging
from pathlib import Path

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor from a config entry."""
    async_add_entities([DevicesFileCountSensor(entry)])


class DevicesFileCountSensor(SensorEntity):
    """Sensor showing number of YAML device configs bundled."""

    _attr_has_entity_name = True
    _attr_translation_key = "device_count"
    _attr_entity_category = EntityCategory.DIAGNOSTIC
    _attr_native_unit_of_measurement = "devices"

    def __init__(self, entry: ConfigEntry) -> None:
        """Initialize sensor."""
        self._attr_unique_id = f"{entry.entry_id}_device_count"
        self._attr_device_info = {
            "identifiers": {(entry.domain, entry.entry_id)},
            "name": entry.title,
        }

    @property
    def native_value(self) -> int:
        """Return the number of YAML files in our devices/ folder."""
        devices_dir = Path(__file__).parent / "devices"
        return len(list(devices_dir.glob("*.yaml")))
