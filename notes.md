# Notes

## DeepReviewer-v2-openai Responses API change

- `DeepReviewer-v2-openai/deepreview/runner.py` now uses `OpenAIResponsesModel` instead of `OpenAIChatCompletionsModel`.
- OpenRouter usage/cost hook now wraps `client.responses.create` instead of `client.chat.completions.create`.
- `OpenAIProvider` is configured with `use_responses=True`.
- Runtime metadata now records `llm_api_mode` as `responses`.
- `DeepReviewer-v2-openai/deepreview/config.py` defaults `OPENAI_USE_RESPONSES_API` to `true`.
- `DeepReviewer-v2-openai/README.md` and `README.zh-CN.md` show `OPENAI_USE_RESPONSES_API=true`.
