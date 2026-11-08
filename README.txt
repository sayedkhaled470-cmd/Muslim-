تحديث تطبيق مسلم على GitHub (ليتثبّت فوق النسخة الموجودة)

1) على GitHub: Add file > Upload files، وارفع هذه الملفات (تحل محل القديمة):
   index.html  package.json  capacitor.config.json  icon.png  icon-fg.png  splash.png  muslim.keystore
2) افتح .github/workflows/build-apk.yml واستبدل محتواه بالكود الكامل (في الرسالة أو في ملف build-apk.yml)، ثم Commit.
3) تبويب Actions > Build APK > Run workflow، ثم نزّل muslim-apk من Artifacts.

مهم: أول مرة فقط لازم تحذف النسخة القديمة من الموبايل وتثبّت الجديدة (لأن مفتاح التوقيع اتغيّر).
من بعدها كل تحديث بيتثبّت فوق القديم من غير حذف وبنفس البيانات.
اجعل الـ Repository خاص (Private) لأن مفتاح التوقيع موجود فيه.
