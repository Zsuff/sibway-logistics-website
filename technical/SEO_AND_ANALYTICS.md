# SEO та аналітика

## Продакшн-домен

У canonical, hreflang, sitemap, Open Graph і schema використовується лише `https://sibway.com.ua`. Preview-домени, GitHub URL та локальні адреси не повинні потрапити у продакшн-розмітку.

## Базове SEO на кожній індексованій сторінці

- Коректний `lang` документа.
- Один змістовний H1.
- Унікальні `title` і `meta name="description"`.
- Canonical URL.
- Open Graph: title, description, URL, image.
- Альтернативні мовні URL: `hreflang="uk"`, `hreflang="en"`, `hreflang="pl"`, `hreflang="x-default"`.
- Зрозумілі alt-тексти для змістовних зображень.
- Schema.org після погодження фактичних даних: Organization/LocalBusiness, WebSite, Service, BreadcrumbList.

## Технічні файли

- `robots.txt` має дозволяти індексацію продакшн-сайту та містити посилання на sitemap.
- `sitemap.xml` має містити тільки канонічні URL, які реально повертають HTTP 200.
- 404-сторінка не повинна індексуватися як звичайна сторінка.

## Аналітика

До підключення погодити GA4, Google Search Console та події: перегляд форми, початок заповнення, успішна заявка, клік телефону і клік месенджера. Ідентифікатори, ключі й доступи не зберігати у публічному Git.
