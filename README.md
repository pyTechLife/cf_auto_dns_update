# cf_auto_dns_update

با این اسکریپ می‌تونید آیپی هایی که اسکنر کلاودفلر براتون پیدا کرده را به صورت اتوماتیک روی ساب دامنه ها ست کنید

نسخه پایتون اسکنر رو از اینجا دانلود کنید :

`https://github.com/MortezaBashsiz/CFScanner`

نتایج در پوشه result ذخیره میشن ما به جدیدترین نتیجه اسکن نیاز داریم، حالا این اسکریپ رو دانلود کنید یا با دستور گیت یا به صورت فایل زیپ

به مسیر روت فایل دانلود شده برید اول پیش نیازها رو نصب کنید با این دستورها :


`sudo pip install cloudflare`

`pip install pandas`

حالا می تونید از این اسکریپ به صورت زیر استفاده کنید :

در گام اول فایل رو با نرم افزار ویرایش گر متن یا هر نرم افزاری که راحت ترید باز کنید و این قسمت ها رو با اطلاعات خواسته شده تکمیل گنید :

`api_key = '####' #your cloudflare token

hostname = '###' #your subdomain 

Number_of_subdomains = 10 #The number of domains that need to be set.

subdomains = 'mtn' # Your subdomain is determined here, for example, you can use mtn for Irancell`

مقدار api_key  رو باید از سایت کلاودفلر بگیرید از این مسیر :
`https://dash.cloudflare.com/profile/api-tokens`

در این قسمت از بخش API Tokens  با کلید Create Token به قسمت مربوطه برید و از جدول بخش Edit zone DNS کلید use template را بزنید در صفحه بعدی بخش Zone Resources یا اکانت خودتون رو انتخاب کنید یا
اگر تنها یک دامنه دارید all zones رو انتخاب کنید، در ادامه continue summary رو بزنید تا به بخش بعدی برید در نهایت کلید create token  رو بزنید و تموم 
عبارتی که بهتون به عتوان توکن نمایش میده رو در قسمت api_key وارد کنید به این صورت :

`api_key = 'birOGxNkdSO25hdijF84vIpqXtdEp59AZpdXS0aw' #your cloudflare token`

در قسمت hostname نام ساب دامنه‌ایی که از قبل ساخته شده رو بذاریداز این بخش برای گرفتن ایدی زون استفاده میشه مهم نیست که کدوم ساب دامنه شماست فقط باید درست باشه

در بخش بعدی که Number_of_subdomains نام داره به جای عدد ۱۰ باید تعداد ساب دامنه هایی که قراره براتون با ایپی ها ایجاد بشه رو تعیین کنید مثلا اگر به ۳ تا ساب دامنه نیاز دارید 
که از ایپی های تمیز براشون استفاده بشه کافیه که عدد سه رو وارد کنید

در بخش subdomains شما باید نام ساب دامنه هایی که اینجاد میشه رو وارد کنید مثلا اگر در مرحله قبل عدد رو ۳ زدید و ایپی های تمیز روی ایرانسله می تونید همون mtn رو بذارید باشه اینجوری
سه تا ساب دامنه به این صورت ساخته میشه :

`mtn1.yourdomain.tk
mtn2.yourdomain.tk
mtn3.yourdomain.tk
`







طبق داکیومنت اسکنر خروجی برنامه شامل یک فایل csv با این ستون هاست :

`ip,`

`avg_download_speed,`

`avg_upload_speed,`

`avg_download_latency,`

`avg_upload_latency,`

به ترتیب:

آیپی تمیز پیدا شده

متوسط سرعت دانلود (مقدار بیشتر بهتر)

متوسط سرعت آپلود (مقدار بیشتر بهتر)

متوسط تاخیر دانلود (مقدار کمتر بهتر)

متوسط تاخیر آپلود (مقدار کمتر بهتر)

این اسکریپ چندتا سوییچ داره که می تونید نتایج بدست اومده رو بر اساس چهار فاکتور (آیپی که مهم نیست) مرتب کنید و بعد استفاده کنید، یعنی مثلا ۵۰ تا ایپی تمیز پیدا شده که شما فقط ده تاش رو لازم دارید 
خب بهتره که مثلا ده تایی رو انتخاب کنید که سرعت دانلود بیشتری داشته باشن

استفاده از سوییچ ها به این صورته :

با سوییچ f- مسیر جدیدترین نتیجه اسکن شامل ایپی های تمیز رو برنامه میدید به عنوان مثال 

`python auto_change_dns.py -f ./result/20230518_124531_result.csv`

در این حالت (بدون سوییچ s- ) ایپی های پیدا شده به صورت پیشفرض با بیشترین سرعت دانلود مرتب میشن 

سوییچ s- مقادیر زیر رو میگیره می تونید یکی رو انتخاب کنید یا اصلا مثل حالت بالا چیزی انتخاب نکنید تا به صورت پیشفرض بر اساس بیشترین سرعت دانلود مرتب بشن :

`ads بیشترین مقدار سرعت دانلود در اولویت باشه
`

`aus بیشترین مقدار سرعت آپلود در اولویت باشه
`

`adl کمترین تاخیر دانلود در اولویت باشه
`

`aul کمترین مقدار تاخیر در آپلود در اولویت باشه
`

به عنوان مثال اگر بخواهیم که لیست ایپی های تمیز پیدا شده با کمترین تاخیر دانلود مرتب بشن از سوییچ s به صورت زیر استفاده می کنیم :


`python auto_change_dns.py -f ./result/20230518_124531_result.csv -s adl`

فعلا همین احتمالا اگر آموزش ویدویی براش ساخته بشه هم براتون اینجا میذارم 






















