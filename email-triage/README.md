# Email Triage Skill Pack

Набор разбит на отдельные навыки, чтобы не смешивать:
- triage ядро
- классификацию
- создание задач в Linear
- обработку рассылок
- tracking waiting-for-response
- генерацию digest
- конфиг и персональные правила

## Структура

- `email-triage-core.md` — основной orchestration skill
- `email-triage-classifier.md` — модель классификации и decision rules
- `email-triage-linear.md` — создание и дедупликация задач в Linear
- `email-triage-newsletters.md` — summary/translation/deep-dive для рассылок
- `email-triage-waiting.md` — логика waiting/follow-up
- `email-triage-digest.md` — финальный русский digest
- `email-triage-queries.md` — поисковые паттерны Gmail
- `email-triage-config.yaml` — настраиваемые правила
- `email-triage-playbook-template.yaml` — файл для калибровки поведения со временем

## Принципы

1. Inbox — это очередь решений, а не система хранения.
2. Не читать full body у всего подряд.
3. Не создавать Linear issue на каждый чих.
4. Reply и Action — разные сущности.
5. Waiting — это не корзина для непонятного.
6. Рассылки обрабатываются отдельно от реальной работы.
7. Никогда ничего не удалять автоматически.
8. Приоритет — минимизировать false-positive task creation.

## Рекомендуемый порядок использования

1. `email-triage-core`
2. `email-triage-classifier`
3. `email-triage-linear` / `email-triage-newsletters` / `email-triage-waiting`
4. `email-triage-digest`

## Что еще надо будет сделать у тебя

- Подставить реальные команды Linear MCP / wrapper, если у тебя есть свой слой вызовов.
- Создать Gmail labels:
  - `triage/action`
  - `triage/reply`
  - `triage/waiting`
  - `triage/read-later`
  - `triage/reference`
  - `triage/finance`
  - `triage/noise`
- Заполнить `email-triage-config.yaml`
- Заполнить `email-triage-playbook-template.yaml` под свои источники шума, VIP-контакты и любимые рассылки.
