تحديث تطبيق مسلم على GitHub

1) افتح الـ Repository على GitHub > Add file > Upload files، وارفع هذه الملفات (هتحل محل القديمة):
   index.html  package.json  capacitor.config.json  icon.png  icon-fg.png
2) افتح الملف .github/workflows/build-apk.yml واستبدل محتواه بالكود الكامل الموجود في الرسالة (أو في ملف build-apk.yml هنا)، ثم Commit.
3) تبويب Actions > Build APK > Run workflow، ثم نزّل muslim-apk من Artifacts.

ملفات الأذان (اختياري): ارفع على نفس المستوى ملفات mp3 بهذه الأسماء بالظبط:
adhan-makkah.mp3  adhan-madinah.mp3  adhan-afasy.mp3  adhan-qatami.mp3  adhan-basit.mp3  adhan-tobar.mp3
