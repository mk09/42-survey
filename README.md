# Folio survey workspace

A Next.js 16 App Router app with TypeScript and React 19.

## Run

```sh
npm install
npm run dev
```

Open http://localhost:3000. On Windows PowerShell, use `npm.cmd` if script execution is restricted.

## Features

- Create projects and surveys within each project.
- Add, edit, duplicate, reorder, and delete open-ended and dropdown questions.
- Edit dropdown options and mark questions required.
- Preview surveys with native form validation.
- Search projects and surveys.
- Browser-local persistence via localStorage.

This version is a local survey builder. It has no authentication, shared database, public survey links, or response collection. Preview submissions are not saved. Clearing browser storage removes your workspace.

## Verification

```sh
npm run typecheck
npm run build
```
