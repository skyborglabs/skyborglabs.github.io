# Domain and Google Play handoff

Confirmed company: SKYBORG ENTERPRISE LLC  
Confirmed website: https://www.skyborglabs.com  
Confirmed contact: admin@skyborglabs.com  
GitHub: https://github.com/skyborglabs/skyborglabs.github.io

## GitHub and Porkbun

1. Publish the repository using GitHub Actions in Settings → Pages.
2. Set the Pages custom domain to `www.skyborglabs.com` before changing DNS.
3. In Porkbun, replace the website parking record for `www` with CNAME `skyborglabs.github.io`.
4. Route the apex `skyborglabs.com` using A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`. Remove conflicting apex parking records. Preserve MX, SPF, DKIM, DMARC, and other mail/verification records. Do not change nameservers.
5. Wait for DNS and GitHub's certificate provisioning, then enable Enforce HTTPS when available.
6. Verify the homepage, game page, video, support, and privacy page without signing in. Check both apex redirect and www HTTPS.

Source: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

## Google website ownership

Use the Google account associated with the Play Console. Add the Domain property `skyborglabs.com` in Google Search Console. Copy the exact TXT value Google supplies to Porkbun at the domain root, then verify it. Do not invent a verification token.

Then request/complete the website association from Play Console. Search Console ownership and Play Console association are separate steps. An association may be approved automatically when the same account owns the Search Console property. Otherwise its verified owner must approve the request.

Source: https://support.google.com/googleplay/android-developer/answer/13205715

Organization registration also requires accurate organization/legal identity, D-U-N-S details, and verified contact information. A website cannot guarantee account approval. Do not publish private identity documents or D-U-N-S data in this repository.

## Email operations and future app privacy

The current newsletter mechanism is an opt-in email request, not an automated signup. Before sending commercial newsletters, establish your mailing-list process, a valid postal sender address, and functioning unsubscribe handling. Never send a marketing message merely because someone contacted support. No newsletters have been sent by this project.

Source: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business

The public privacy page covers this website and email communications. Before an app release, describe the app's actual SDKs, ads, purchases, data collection/sharing/deletion and child-audience practices in an app-specific policy and consistent Google Play Data safety declarations. Do not submit the current website policy as if it describes an unreleased app's future implementation.

Source: https://support.google.com/googleplay/android-developer/answer/10144311

Add app-ads.txt only when an actual ad network supplies your authorized seller records. No publisher ID or store links have been invented. Add news, demos, press materials, events, music, cards and apparel pages when real content is available.
