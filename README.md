# Tuya Local — My Devices

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

Дополнительные конфигурации устройств для [tuya_local](https://github.com/make-all/tuya-local).

При запуске Home Assistant интеграция копирует YAML-файлы из `devices/` в `custom_components/tuya_local/devices/`.

## Установка через HACS

1. HACS → Интеграции → ⋮ → **Добавить пользовательский репозиторий**
2. URL: `https://github.com/astrizhenyuk/tuya-local-my-devices`
3. Тип: **Integration**
4. Установить → Перезагрузить Home Assistant

## Добавление устройств

YAML-файлы клади в `custom_components/tuya_local_my_devices/devices/` — после обновления через HACS и перезагрузки HA они автоматически попадут в `tuya_local/devices/`.

## Устройства

| Устройство | Модель | DP ID |
|---|---|---|
| Timberk Smart Humidifier | T-HU5-A101E-WF | qnwki7iygqaaxaft |
