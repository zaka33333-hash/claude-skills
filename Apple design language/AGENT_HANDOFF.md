# 🤖 Agent Handoff Briefing: Star Toner Project 

**To the AI Agent reading this:** 
The user (who recently took over running the store from their father) is working on a high-end, conversion-optimized Shopify redesign for `star-toner.com` paired with an aggressive SEO turnaround. **Read this entire document before taking action.**

## 1. Project Context & Aesthetic Rules
- **Brand:** Star Toner (Spain-based distributor of compatible toner and ink).
- **Design Language:** "Liquid Glass" / Apple-inspired. Dark theme (`#000` background). 
- **Tech Stack:** Vanilla HTML/CSS/JS (Shopify Custom Liquid sections).
- **Key UI Patterns:** `backdrop-filter` glassmorphism, spring physics on hover, `.cl-` or `.hero-` prefixed classes to avoid Dawn theme collisions, glowing effects. 
- **CRITICAL RULE:** *Never* write generic, cheap-looking CSS. Always aim for a $1M premium aesthetic.

## 2. Current Code State
We have been editing files locally in the `Apple design language` folder.
- `hero-pro-FINAL.html`: The Hero section.
  - *Recent changes:* Optimized mobile performance. Added `fetchpriority="high"` and explicit dimensions to the LCP image. Disabled expensive `backdrop-filter: blur(28px)`, parallax JS, and infinite RGB `requestAnimationFrame` loops on mobile (`max-width: 900px`) to fix a 41% Mobile PageSpeed score.
- `collections-FINAL.html`: The Collections grid.
  - *Pending:* Needs the exact same mobile performance optimizations applied (disabling expensive GPU CSS filters and parallax JS for touch devices).

## 3. SEO Crisis & Findings (The Reality Check)
We performed a deep GSC and PageSpeed audit today. 
- **The Good:** Sherpas Smart SEO app is installed and working perfectly (100/100 on-page SEO score). The 10 existing blog posts were successfully verified and look great. 
- **The Bad:** 
  - **Domain Authority is 1 / 100.** This is the #1 reason the site gets only ~30 organic clicks/month.
  - **1,133 pages are Not Indexed** in Google Search Console. 187 of these are "Crawled - currently not indexed" (mostly product pages lacking authority/unique reviews).
  - 48 pages are hitting 404s. 
  - Several typos in the main Shopify navigation menu (`Cartuchod de tinta`, `Impresoras Lserjet`).

## 4. Priority Action List for the Next Session

When the user says "Let's continue", pick up exactly here:

### Code/Design (Immediate):
1. **Optimize `collections-FINAL.html` for Mobile Speed:** Strip down the expensive `backdrop-filter` and parallax JS calculations on mobile screens, strictly following the pattern we used in the hero file to reduce CPU/GPU load.
2. **Build the remaining sections:** Check if "Shop by Brand" or the "SEO Info" sections need to be built or integrated into Shopify next.

### SEO/Growth (Next Steps):
1. **Fix Typos:** Remind the user to fix "Cartuchod" and "Lserjet" in the Shopify Admin Navigation menu.
2. **404 Redirects:** Help the user map the 48 dead URLs to 301 redirects to recover crawl budget.
3. **Domain Authority Engine:** Work with the user to start generating localized backlinks (Google Business Profile, local directories, supplier backlinks) to push DA from 1 to 15+. 
4. **Content:** Draft internal linking structures for the 10 existing blog posts to push authority directly to the product collection pages.

---
**Agent Directive:** Do not apologize, do not hallucinate. Parse the user's immediate request against this handoff, and start writing code or executing the SEO strategy immediately. Maintain a professional, highly competent, senior-developer tone.
