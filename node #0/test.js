setTimeout(function () {
		 console.log('자.. 프로세스는 죽지 않았습니다.');
		  setTimeout(function() {
			     console.log('난 아직도 죽지 않았습니다.');
				  }, 5000); // 5초 뒤에 또 실행
		  }, 5000); // 5초뒤에 실행
// 강제적으로 프로세스 에러 발생시킴
// 존재하지 않는 함수 실행
nonExistentFunc(); // or tow new Error('나 에러!!');
// 에러지점 이하의 코드는 실행되지 않습니다.
console.log('이 부분은 console에 보여지지 않습니다.');
