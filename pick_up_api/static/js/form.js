$(document).ready(()=>{
  //
  var car_name = []
  var car_latitude = []
  var car_longitude = []
  //
  var client_name = []
  var client_latitude = []
  var client_longitude = []
  //
  console.log('Console ajax file ..')
  //
  $('.action-submit').click(()=>{
    //
    console.log('action ..')
    //
    $('.outil_car').children().each((index,value)=>{
      //
      //console.log('index ..',index)
      //
      $(value).children('input').each((idx,value)=>{
        //
        //console.log('index input ..',$(value))
        //console.log('index input ..',$(value).val())
        //
        if(idx == 0) car_name.push($(value).val())
        if(idx == 1) car_latitude.push($(value).val())
        if(idx == 2) car_longitude.push($(value).val())
        //
      })
      //
      //
    })
    //
    $('.outil_client').children().each((index,value)=>{
      //
      //console.log('index ..',index)
      //
      $(value).children('input').each((idx,value)=>{
        //
        //console.log('index input ..',$(value))
        //console.log('index input ..',$(value).val())
        //
        if(idx == 0) client_name.push($(value).val())
        if(idx == 1) client_latitude.push($(value).val())
        if(idx == 2) client_longitude.push($(value).val())
        //
      })
      //
      //
    })
    //Driver information
    console.log('car name ==>',car_name)
    console.log('car latutude ==>',car_latitude)
    console.log('car longitude ==>',car_longitude)
    //Client information
    console.log('client name ==>',client_name)
    console.log('client latutude ==>',client_latitude)
    console.log('client longitude ==>',client_longitude)
    // create data
    const data = {
          clients:client_name.join(),
          l:client_latitude.join(),
          g:client_longitude.join(),
          cars:car_name.join(),
          cl:car_latitude.join(),
          ci:car_longitude.join(),
          wilaya:'Alger',
          slot:'12:00'
       }
    //Ajax post
    $.ajax({
       //
       type:'POST',
       url:'/pick_up/',
       data:data,
       success:function(response){
          //
          //sol ==> {
          //"k": {
          //"coordonne": [2.58, 3.25],
          //"sol": [{"name": "m", "coordonne": [2.587, 3.569]},{"name": "n", "coordonne": [2.78, 3.69]}]
          //}
          //}
          console.log('sol ==>',response)
          const resultat = JSON.parse(response)
          console.log('resultat ==>',resultat)
          const keys = Object.keys(JSON.parse(response))
          let html = ""
          //show resultat card
          keys.forEach((car)=>{
            //
            if (car != 'iframe'){
              //
              resultat[car].sol.forEach((client)=>{
                html += `<h3>${client.name}</h3>`
              })
              //template show
              $('#car_card').append(
                `
              <div class="chauf">
                <h3>${car}</h3>
                <div class="clients">
                  ${html}
                </div>
              </div>
               `
              )
              //
            }
            //
          })
          //show map 
          $('#map').html(resultat.iframe)
       }
       //
    })
  })
  //
 })