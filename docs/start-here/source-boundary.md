# Notion Source Boundary

## Allowed root

- Title: `Microsoft Technical Archive`
- Page ID: `36bdbd59-1ead-80a0-be5d-d0cc9d468183`
- URL: `https://app.notion.com/p/36bdbd591ead80a0be5dd0cc9d468183`

## Allowed content

- The root page itself
- Pages, databases, and files whose ancestor chain is under the allowed root
- Images and attachments embedded in allowed pages

## Explicitly excluded

- `Project Archive`
- Customer-specific project pages
- Project execution records
- Customer names, tenant data, internal architecture, and evidence artifacts
- Any page whose ancestor chain cannot be verified under the allowed root

## Retrieval rule

Every Notion search must use the allowed root as `page_url`.
Every fetched result must be rejected when its ancestor path is outside the allowed root.
