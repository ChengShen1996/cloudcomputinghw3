var apigClient;
var bucket_url = 'https://s3.amazonaws.com/image0428/';
window.onload = function(){

	AWS.config.region = 'us-east-1'; 
	apigClient = apigClientFactory.newClient({
		apiKey: 'CacZ2WkqJ57lvOVlSUSgK17SSPmHKQgQ1DUunbQe'
    });

    $('#search').click(function(e) {
    	$('.search_res').remove();
      var text = $('#query').val();
      search_pic(text);
    });

    $('#upload').click(function(e) {
    	e.preventDefault();
      img = $('#image').prop('files')[0];
      upload_pic(img);
    });

}

function search_pic(text){
	console.log("Search");
  param = {
  	"q":text
  };
  apigClient.searchGet(param)
    .then(function(result){
    	console.log(result);
    	imgs = result.data.hits.hits;
    	for (i=0; i<imgs.length;i++){
    		img = imgs[i]._source.objectKey;
				console.log(img)
    		add_pic(img);
    	}

    });
}

function add_pic(img){
	img = bucket_url + img;

	text = '<div class="col-lg-3 col-md-4 col-xs-6 thumb search_res"><img  src="'+img+'" class="zoom img-fluid "  alt=""></div>'
	console.log(text);
	$('#gallery').append(text);
}

function upload_pic(img){

  // var fileReader = new FileReader();

  // fileReader.onloadend = function(fileLoadedEvent) {
		// console.log("Convert");
  //   var srcData = fileLoadedEvent.target.result; // <--- data: base64
  //   console.log("Upload");
  //   console.log(img);
  //   param = {
  //     'Content-Type': img.type,
  //     'object' : img.name,
  //     'x-api-key': 'CacZ2WkqJ57lvOVlSUSgK17SSPmHKQgQ1DUunbQe'
  //   }

  //   body = img;

  //   apigClient.uploadPut(param,body).then(function(result){
  //     console.log(result)
  //   });

  // }

  // fileReader.readAsDataURL(img);
  console.log("Upload");
  var xhr = new XMLHttpRequest();
  xhr.open("PUT", "https://cx8bp5m735.execute-api.us-east-1.amazonaws.com/beta/upload?object="+ img.name);
  xhr.setRequestHeader("Content-Type", img.type);
  xhr.setRequestHeader("x-api-key", "CacZ2WkqJ57lvOVlSUSgK17SSPmHKQgQ1DUunbQe");
  xhr.send(img);
}