$(document).ready(()=>{
  //
  $('#add').on('click',()=>{
    //
    console.log('add new client')
    //
    const client = prompt('client name')
    const latitude = prompt('latitude')
    const longitude = prompt('longitude')
    //
    const data = {
       client:client,
       l:latitude,
       g:longitude
    }
    //
    console.log('data =>',data)
    //
    if(client && latitude && longitude){
     //
     $.ajax({
      //
      type:'POST',
      url:'/pick_add/',
      data:data,
      success:function(response){
        //
        console.log('resultat =>',response)
        //
        const resultat = JSON.parse(response)
        const sol = resultat['sol']
        const keys = Object.keys(sol)
        //
        $('#car_card').html('')
        //
        keys.forEach((key)=>{
          //
          let html =''
          //
          console.log('solution ==>',sol[key]['sol'])
          sol[key]['sol'].forEach((client)=>{
            //
            html +=`<h3>${client}</h3>`
            //
          })
          //template show
          $('#car_card').append(
          `
          <div class="chauf">
             <h3>${key}</h3>
             <div class="clients">
                  ${html}
             </div>
          </div>
          `
          )
          //
        })
        //show map
        $('#map').html('')
        $('#map').html(resultat['iframe'])
      }
      //
    })
     //
    }
    //
  })
  //
})