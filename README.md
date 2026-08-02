# 👤 LinkedIn Profile API: Public Profiles to Structured JSON

> The most efficient, reliable, and developer-friendly way to use the LinkedIn Profile API.

**Actor page:** [apify.com/johnvc/linkedin-profile-api](https://apify.com/johnvc/linkedin-profile-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/linkedin-profile-api/input-schema](https://apify.com/johnvc/linkedin-profile-api/input-schema?fpr=9n7kx3)

Send one or many public LinkedIn profile URLs and get back one clean JSON row per person: name, headline, location, current company and title, work experience, education, and follower counts. It is built API-first and MCP-ready, so you can call it from Python or drive it as a tool from an AI agent.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-LinkedIn-Profile-API.git
   cd Apify-LinkedIn-Profile-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python linkedin-profile-api-example.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python linkedin-profile-api-example.py
```

## Why Use This LinkedIn Profile API?

**A URL in, structured data out.** You never touch collection infrastructure. Pass a public profile URL and get flat, predictable fields you can load straight into a sheet, a database, or a CRM.

**Batch friendly.** Send up to 1000 profile URLs in one run. They are collected in parallel and returned one row each, so enriching a list is one call.

**Pay per profile.** Billing is per profile returned, with no per-run setup fee, so you only pay for what is delivered.

**Reliable and predictable.** Every profile comes back with the same field shape, and a URL that cannot be collected returns a clear error row instead of failing the whole run.

**MCP-ready.** Call it as a tool from Claude, Cursor, and other AI agents (see the install sections below).

## Features

### Core Capabilities
- Collect one or many public LinkedIn person profiles by URL
- Name, headline, about, location, current company and title
- Full work experience and education history
- Follower and connection counts, profile photo URL, public profile URL

### Data Quality
- One consistent JSON row per profile, every time
- A plain-language `summary` field on every row for quick scanning and AI use
- Clear per-URL error rows so a single bad link never sinks the batch

## Usage Examples

### Basic Example
```json
{
  "profileUrls": ["https://www.linkedin.com/in/satyanadella"]
}
```

### Batch Example (collected in parallel)
```json
{
  "profileUrls": [
    "https://www.linkedin.com/in/satyanadella",
    "https://www.linkedin.com/in/williamhgates"
  ]
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `profileUrls` | `list[str]` | YES | - | One or more public LinkedIn `/in/` profile URLs. Up to 1000 per run; non-`/in/` URLs are skipped. |

## Output Format

Each profile is returned as one JSON row:

```json
{
  "result_type": "profile",
  "name": "Satya Nadella",
  "headline": "Chairman and CEO at Microsoft",
  "currentCompany": "Microsoft",
  "currentTitle": "Chairman and CEO",
  "location": "Redmond, Washington, United States",
  "countryCode": "US",
  "followers": 12056751,
  "connections": 500,
  "pastCompanies": ["Microsoft", "University of Chicago", "Starbucks"],
  "education": [{ "title": "The University of Chicago Booth School of Business" }],
  "email": null,
  "publicUrl": "https://www.linkedin.com/in/satyanadella",
  "summary": "Chairman and CEO at Microsoft, based in Redmond, Washington, United States, 12,056,751 followers"
}
```

The `email` field is always `null`; email is not available from this source.

---

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the LinkedIn Profile API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-profile-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the LinkedIn Profile API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

---

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-profile-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-profile-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the LinkedIn Profile API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

---

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/linkedin-profile-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-profile-api`, using OAuth when prompted.
5. Ask Claude to run the LinkedIn Profile API.

Open Claude on the web: https://claude.ai/referral/uIlpa7nPLg

---

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-profile-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-profile-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the LinkedIn Profile API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

---

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-profile-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the LinkedIn Profile API to power your data workflows with reliable, structured results.*

Last Updated: 2026.08.02
