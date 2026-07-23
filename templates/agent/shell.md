# Shell: Anthropic Messages API

Everything Anthropic-specific for this agent. `system-prompt.md` is passed as
the `system` parameter; nothing below changes the content.

```yaml
model: <exact model ID>          # pin the version an eval was run against
max_tokens: <n>
temperature: <t>
# thinking, stop_sequences, etc. as needed
```

## Tool schemas

<The tools from tools.md, expressed as Anthropic tool-use JSON schemas, or a
pointer to where they're defined in `src/`. Schema syntax lives here, not
in the manifest.>

## Assembly

<How src/ builds the request: system = system-prompt.md, messages = ...,
tools = ... . Point at the code that does it.>
