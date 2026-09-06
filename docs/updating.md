# Обновление Research Dossier

## Установленная версия из GitHub

Один раз добавьте marketplace из публичного репозитория:

```bash
codex plugin marketplace add abbnv/research-dossier --ref main
codex plugin add research-dossier@research-skill
```

Чтобы получить новые версии:

```bash
codex plugin marketplace update research-skill
codex plugin add research-dossier@research-skill
```

Если Codex сообщает, что плагин уже установлен, сначала удалите только установленную копию и добавьте её снова:

```bash
codex plugin remove research-dossier@research-skill
codex plugin add research-dossier@research-skill
```

После установки откройте новую задачу Codex. Уже открытая задача может продолжать использовать инструкции, загруженные в начале разговора.

## Локальная разработка

Из корня репозитория прочитайте имя marketplace и обновите cache-buster для локальной итерации:

```bash
python3 /Users/aleksandrbubnov/.codex/skills/.system/plugin-creator/scripts/read_marketplace_name.py \
  --marketplace-path .agents/plugins/marketplace.json
python3 /Users/aleksandrbubnov/.codex/skills/.system/plugin-creator/scripts/update_plugin_cachebuster.py \
  plugins/research-dossier
codex plugin add research-dossier@research-skill
```

`update_plugin_cachebuster.py` нужен только для локальной разработки, чтобы Codex не использовал старый кэш. В публичном репозитории сохраняйте обычную семантическую версию вроде `0.2.0`, а не локальный cache-buster.

## Что проверять перед публикацией

```bash
python3 -m unittest discover -v
python3 /Users/aleksandrbubnov/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  plugins/research-dossier/skills/research
python3 /Users/aleksandrbubnov/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py \
  plugins/research-dossier
```

Публикуйте изменения в `main` только после проверки контракта репозитория и нового примера.
