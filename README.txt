تحديث تطبيق مسلم على GitHub

1) الـ Repository > Add file > Upload files، وارفع هذه الملفات (تحل محل القديمة):
   index.html  package.json  capacitor.config.json  icon.png  icon-fg.png  splash.png
2) افتح .github/workflows/build-apk.yml واستبدل محتواه بالكود الكامل (موجود في الرسالة وفي ملف build-apk.yml هنا)، ثم Commit.
3) تبويب Actions > Build APK > Run workflow، ثم نزّل muslim-apk من Artifacts.

ملفات الأذان (اختياري): ارفع بجانبهم ملفات mp3 بهذه الأسماء:
adhan-makkah.mp3  adhan-madinah.mp3  adhan-afasy.mp3  adhan-qatami.mp3  adhan-basit.mp3  adhan-tobar.mp3
