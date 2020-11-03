//ajax 환율정보 불러오기
$.ajax({
    type: "GET",
    url: "https://api.manana.kr/exchange/rate.json",
    data: {},
    success: function (response) {
        let rate = response[1]['rate'];
        let tempText =  `<p class="gray-font">달러 원 환율 : ${rate} </p>`;
        //검색 결과 나타난 정보를 표시
        $('#exchange').append(tempText);
        }
    })

