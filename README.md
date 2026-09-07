# Brand Studio — brand.sadaorg.com

The website and backend behind [brand.sadaorg.com](https://brand.sadaorg.com): upload a logo, get a whole brand. Bilingual Arabic and English.

## Layout

```
docs/     the site (static, served by nginx)
server/   Flask backend: extraction, gpt-image-1 generation jobs,
          guideline deck builder, Moyasar paywall
examples/ the Terra demo brand
```

## Deploy

- Static: rsync `docs/` to `/var/www/brand`
- Backend: rsync `server/` to `/opt/brand-extract`, then `systemctl reload brand-extract`
- Env (`/opt/brand-extract/.env`): `OPENAI_API_KEY`, `MOYASAR_SK`, `CHROME_BIN=google-chrome`, `IMAGE_QUALITY=medium`

The Claude Code skill that powers the method lives in
[brand-identity-generator](https://github.com/AbdulkareemKR/brand-identity-generator).

MIT.
