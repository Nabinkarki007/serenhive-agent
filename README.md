# SerenHive Agent

Autonomous marketing control plane for SerenHive, a Korean skincare business in Nepal.

## Recommended stack

- **Postiz (`gitroomhq/postiz-app`)** — social publishing, scheduling, media, analytics and agent/API integration.
- **n8n** — orchestration: research → content plan → generation → safety checks → Postiz.
- **LLM** — strategy, writing, classification and comment triage.
- **FFmpeg + a video renderer** — short-form video assembly.
- **PostgreSQL** — agent memory, product/FAQ knowledge and audit records.
- **Meta APIs/webhooks** — Instagram/Facebook comments and messaging where permitted by account/app permissions.

Postiz is the publishing layer, not the business brain. This repository is the SerenHive-specific control plane and knowledge base.

## Target architecture

```text
                         SERENHIVE AGENT
                               |
        +----------------------+----------------------+
        |                      |                      |
     RESEARCH              KNOWLEDGE              ANALYTICS
        |                      |                      |
   trends/news           products/FAQs          post metrics
   Nepal topics          brand voice            engagement
   competitor signals    policies               winning hooks
        |                      |                      |
        +----------------------+----------------------+
                               |
                         CONTENT PLANNER
                               |
                    +----------+----------+
                    |                     |
                 TEXT                  VIDEO
                    |                     |
               captions              script/voice
               carousel              visuals/subtitles
                    +----------+----------+
                               |
                         SAFETY GATE
                               |
              +----------------+----------------+
              |                                 |
          LOW RISK                         SENSITIVE
              |                                 |
        auto schedule                    human approval
              |                                 |
              +----------------+----------------+
                               |
                             POSTIZ
                               |
                Instagram / Facebook / TikTok
                               |
                    analytics + inbox events
                               |
                         LEARNING LOOP
```

## Autonomy policy

### Auto
- Research topics and trends.
- Draft educational posts and captions.
- Generate approved video formats.
- Schedule/publish content through official platform integrations.
- Answer low-risk product/FAQ comments when the answer exists in the approved knowledge base.

### Human approval required
- Medical/health claims.
- Adverse reactions or safety complaints.
- Refund/payment/legal complaints.
- New product claims not present in the knowledge base.
- Influencer disputes or sensitive public replies.
- Promotional campaigns outside predefined rules.

### Platform rule

Do not use password-based browser bots or scraping to impersonate a user. Use official OAuth/API integrations. Platform capabilities vary; publishing and comment-management permissions are not identical across Instagram, Facebook and TikTok.

## SerenHive knowledge base

Keep business truth in version-controlled files:

```text
knowledge/
  brand.md
  voice.md
  policies.md
  products/
  faq/
  skincare/
  content-rules.md
  prohibited-claims.md
```

The agent should answer from these files/database first and use web research for fresh information.

## First milestone

1. Deploy Postiz.
2. Connect SerenHive Instagram, Facebook and TikTok through official platform authentication.
3. Deploy n8n.
4. Add SerenHive knowledge files.
5. Build one daily research workflow.
6. Build one content-generation workflow.
7. Start with human approval for every post.
8. After 2–4 weeks of reliable results, allow low-risk educational posts to auto-publish.

## Upstream project

Postiz: https://github.com/gitroomhq/postiz-app

This repository should contain SerenHive-specific automation and policy, while upstream Postiz remains the maintained publishing engine.
