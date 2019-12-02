id='53551'
rows='29'
#final_file='design.txt'
response=$(curl 'http://internshala.com/employer/paginated_applications/'$id -H 'Cookie: PHPSESSID=53jsksibs1oeu6oejoonpsjmt0; u=1; l=38E838C9-833B-78A2-6BB1-5FD32C2EAE74%2FCE4EC8D9-ED34-B53C-C041-5237BA34893E; applications_notifications=0; AWSELB=1BC35F8D0EBAEA4A8A17DC9DE5460C4922951E69E33877C47577AB2E49802A0F10C344164551ED284952E81812815A141A7CCF44D0405BB9F216B00FA19224413058E9B1DE; csrf_cookie_name=da6e35635e1ab850a1b29ce4e5f863eb' -H 'Chrome-Proxy: ps=1457084440-1109165881-2981698401-3445588109, sid=75da0b7052a86355b6ac187c0622497b, c=win, b=2564, p=116' -H 'Origin: http://internshala.com' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: */*' -H 'Referer: http://internshala.com/employer/dashboard' -H 'X-Requested-With: XMLHttpRequest' -H 'Proxy-Connection: keep-alive' --data 'rows='$rows'&offset=0&sid=created_at&sord=DESC&status=open&internshala_filter=false' --compressed | ./JSON.sh | egrep '\["view"]')
#view= $(node -pe 'JSON.parse(process.argv[1]).view' $response)
#echo $view
#printf "%s" $response
rm -rf html.txt
touch html.txt
echo ${response:8} > html.txt
sed -i -e 's/\\n//g' html.txt
sed -i -e 's/\\//g' html.txt
sed -i -e 's/^"\(.*\)"$/\1/' html.txt
sed -i -e 's/\(<tr class = \"tr1 CSSRow\">\)\(<\/tr>\)/\n\n/g' html.txt

# sed -i -e  's/.*<span class="application_name">\(.*\)<\/span>.*/\1/g' \
# 	   -e  's/.*<div style="display:none;" class="email">\(.*\)<\/div>.*/\1/g' html.txt
#sed -i -e  's/.*<div style="display:none;" class="email">\(.*\)<\/div>.*/\1/g' html.txt
#sed -i -e 's/<[^>]*>//g' html.txt
python ./html_parser.py html.txt > final.txt