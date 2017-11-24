

$( document ).ready(
  function() {

    var allText = "";
    var numOfFilesOk = 0;
    var numOfFiles = 0;
    var arrText = [];
    var numberfWords = [];

    var pre = document.querySelector("pre");
    
    var makeGraphics = function(){
      var popCanvas = $("#canvas");
      var barChart = new Chart(popCanvas, {
      type: 'bar',
      data: {
        labels: arrText,//["China", "India", "United States", "Indonesia", "Brazil", "Pakistan", "Nigeria", "Bangladesh", "Russia", "Japan"],
        datasets: [{
          label: 'Frecuencia',
          data: numberfWords,//[1379302771, 1281935911, 326625791, 260580739, 207353391, 204924861, 190632261, 157826578, 142257519, 126451398],
          backgroundColor: [
            'rgba(255, 99, 132, 0.6)',
            'rgba(54, 162, 235, 0.6)',
            'rgba(255, 206, 86, 0.6)',
            'rgba(75, 192, 192, 0.6)',
            'rgba(153, 102, 255, 0.6)',
            'rgba(255, 159, 64, 0.6)',
            'rgba(255, 99, 132, 0.6)',
            'rgba(54, 162, 235, 0.6)',
            'rgba(255, 206, 86, 0.6)',
            'rgba(75, 192, 192, 0.6)',
            'rgba(255, 99, 132, 0.6)',
            'rgba(54, 162, 235, 0.6)',
            'rgba(255, 206, 86, 0.6)',
            'rgba(75, 192, 192, 0.6)',
            'rgba(153, 102, 255, 0.6)',
            'rgba(255, 159, 64, 0.6)',
            'rgba(255, 99, 132, 0.6)',
            'rgba(54, 162, 235, 0.6)',
            'rgba(255, 206, 86, 0.6)',
            'rgba(75, 192, 192, 0.6)',
            'rgba(255, 99, 132, 0.6)',
            'rgba(54, 162, 235, 0.6)',
            'rgba(255, 206, 86, 0.6)',
            'rgba(75, 192, 192, 0.6)',
            'rgba(153, 102, 255, 0.6)',
            'rgba(255, 159, 64, 0.6)',
            'rgba(255, 99, 132, 0.6)',
            'rgba(54, 162, 235, 0.6)',
            'rgba(255, 206, 86, 0.6)',
            'rgba(75, 192, 192, 0.6)',
            'rgba(255, 99, 132, 0.6)',
            'rgba(54, 162, 235, 0.6)',
            'rgba(255, 206, 86, 0.6)',
            'rgba(75, 192, 192, 0.6)',
            'rgba(153, 102, 255, 0.6)',
            'rgba(255, 159, 64, 0.6)',
            'rgba(255, 99, 132, 0.6)',
            'rgba(54, 162, 235, 0.6)',
            'rgba(255, 206, 86, 0.6)',
            'rgba(75, 192, 192, 0.6)',
            'rgba(153, 102, 255, 0.6)'
          ]
        }]
        }
      });
    };

    var countWords = function(){
      var a = arrText;
      var s = allText;
      var x, i, output = {};
      for (x = 0; x < a.length; x++) {
          i = 0;
          output[a[x]] = 0;
          while ((i = s.indexOf(a[x], i)) > -1) {
              output[a[x]]++;
              i++
          }
          numberfWords[x] = output[a[x]];
      }
      makeGraphics();
    };

    document.querySelector("input[type=file]").addEventListener("change", function(event) {
    var uploadFile = function(file, path) {
      // handle file uploading
      //console.log(file, path);
      var reader = new FileReader();
      reader.addEventListener("load", function(e) {
        //pre.textContent +="\n" +e.target.result;
        allText += "\n"+e.target.result;
        numOfFilesOk++;
        if( numOfFilesOk ==  numOfFiles ){
          countWords();
        }
      });
      reader.readAsText(file)
    };

    var iterateFilesAndDirs = function(filesAndDirs, path) {
      for (var i = 0; i < filesAndDirs.length; i++) {
        if (typeof filesAndDirs[i].getFilesAndDirectories === 'function') {
          var path = filesAndDirs[i].path;

          // this recursion enables deep traversal of directories
          filesAndDirs[i].getFilesAndDirectories()
          .then(function(subFilesAndDirs) {
            // iterate through files and directories in sub-directory
            iterateFilesAndDirs(subFilesAndDirs, path);
          });
        } else {
          uploadFile(filesAndDirs[i], path);
        }
      }
    };
    arrText = [];
    var textarea = $("textarea").val();
    if(textarea.trim() == ""){
      alert("Intruduce la lista de palabras a ser escanedas");
      return;
    }else{
      arrText = textarea.split(",");
      if ("getFilesAndDirectories" in event.target) {
        event.target.getFilesAndDirectories()
          .then(function(filesAndDirs) {
            iterateFilesAndDirs(filesAndDirs, '/');
          })
      } else {
        // do webkit stuff
        var files = event.target.files;
        numOfFiles =  files.length;
        for (var i = 0; i < files.length; i++) {
          (function(file) {
            uploadFile(file)
          }(files[i]))
        }
      }
    }
  })
 })