jQuery(function($) {
	removeAll();

	intEventsToRadioButtons();
	intEventsToButtons();
	callSum();
});

function intEventsToRadioButtons(){
	$('#sumaRadio').on("change",
						function(){ 
							callSum();
						});
	$('#mulRadio').on("change",
						function(){ 
							callMul();
						});
	$('#divRadio').on("change",
						function(){ 
							callDiv();
						});
	$('#modRadio').on("change",
						function(){ 
							callMod();
						});
	$('#expRadio').on("change",
						function(){ 
							callExp();
						});
}

function intEventsToButtons(){
	$('#btnSum').on('click', function(event) {
	  	var operacion = new Operacion();
	  	var a = parseInt( $('#aSum').val() );
	  	var b = parseInt( $('#bSum').val() );
	  	a = operacion.getBinario(a);
        b = operacion.getBinario(b);
	  	var c = operacion.exeSuma(a,b);
	  	c = parseInt(c, 2);
	  	
	  	$('#cSum').readonly="false"
	  	$('#aSumBin').readonly="false"
	  	$('#bSumBin').readonly="false"
	  	$('#cSumBin').readonly="false"
	  	
	  	$('#cSum').val( c );
	  	$('#aSumBin').val( a );
	  	$('#bSumBin').val( b );
	  	$('#cSumBin').val( operacion.getBinario(c) );

	  	$('#cSum').readonly="true";
	  	$('#aSumBin').readonly="true";
	  	$('#bSumBin').readonly="true";
	  	$('#cSumBin').readonly="true";

	  	//var arr = new Array(10,55,88,89,90,110,155);
	  	//var brr = new Array(11,58,98,189,190,220,256);
	  	//operacion.getMedia(arr,brr);
	});

	$('#btnMul').on('click', function(event) {
	  	var operacion = new Operacion();
	  	var a = parseInt( $('#aMul').val() );
	  	var b = parseInt( $('#bMul').val() );
	  	var c = operacion.exeMul(a,b);
	  	c = parseInt(c, 2);
	  	
	  	$('#cMul').readonly="false"
	  	$('#aMulBin').readonly="false"
	  	$('#bMulBin').readonly="false"
	  	$('#cMulBin').readonly="false"
	  	
	  	$('#cMul').val( c );
	  	$('#aMulBin').val( operacion.getBinario(a) );
	  	$('#bMulBin').val( operacion.getBinario(b) );
	  	$('#cMulBin').val( operacion.getBinario(c) );

	  	$('#cMul').readonly="true";
	  	$('#aMulBin').readonly="true";
	  	$('#bMulBin').readonly="true";
	  	$('#cMulBin').readonly="true";
	});

	$('#btnDiv').on('click', function(event) {

		var operacion = new Operacion();
	  	var a = parseInt( $('#aDiv').val() );
	  	var d = parseInt( $('#dDiv').val() );
	  	var qr = operacion.exeDiv(a,d);

		$('#qDiv').readonly="false";
		$('#rDiv').readonly="false";
	  	/*$('#aDivBin').readonly="false";
	  	$('#dDivBin').readonly="false";
	  	$('#qDivBin').readonly="false";
	  	$('#rDivBin').readonly="false";*/
	  	
	  	
	  	$('#qDiv').val( qr[0] );
	  	$('#rDiv').val( qr[1] );
	  	/*$('#aDivBin').val( operacion.getBinario(a) );
	  	$('#dDivBin').val( operacion.getBinario(d) );
	  	$('#qDivBin').val( operacion.getBinario(qr[0]) );
	  	$('#rDivBin').val( operacion.getBinario(qr[1]) );*/

	  	$('#qDiv').readonly="true";
		$('#rDiv').readonly="true";
	  	/*$('#aDivBin').readonly="true";
	  	$('#dDivBin').readonly="true";
	  	$('#qDivBin').readonly="true";
	  	$('#rDivBin').readonly="true";*/
	  	
	});

	$('#btnMod').on('click', function(event) {
	  	var operacion = new Operacion();
	  	var b = parseInt( $('#bMod').val() );
	  	var exp = parseInt( $('#expMod').val() );
	  	var m = parseInt( $('#mMod').val() );
		exp = operacion.getBinario(exp);
	  	var x = operacion.exeMod(b,exp,m);
	  	
	  	$('#expModBin').readonly="false"
	  	$('#mResultado').readonly="false"
	  	
	  	$('#expModBin').val( exp );
	  	$('#mResultado').val( x );

	  	$('#expModBin').readonly="true"
	  	$('#mResultado').readonly="true"
	});
}

function callSum(){
	if( $('#sumaRadio').is(":checked") ){
		removeAll();

		$('#cSum').readonly="false"
	  	$('#aSumBin').readonly="false"
	  	$('#bSumBin').readonly="false"
	  	$('#cSumBin').readonly="false"
	  	
	  	$('#cSum').val('');
	  	$('#aSum').val('');
	  	$('#bSum').val('');
	  	$('#aSumBin').val('');
	  	$('#bSumBin').val('');
	  	$('#cSumBin').val('');

	  	$('#cSum').readonly="true";
	  	$('#aSumBin').readonly="true";
	  	$('#bSumBin').readonly="true";
	  	$('#cSumBin').readonly="true";

		$('#divSuma').show();
	}
}

function callMul(){
	if( $('#mulRadio').is(":checked") ){
		removeAll();

		$('#cMul').readonly="false"
	  	$('#aMulBin').readonly="false"
	  	$('#bMulBin').readonly="false"
	  	$('#cMulBin').readonly="false"
	  	
	  	$('#cMul').val('');
	  	$('#aMul').val('');
	  	$('#bMul').val('');
	  	$('#aMulBin').val('');
	  	$('#bMulBin').val('');
	  	$('#cMulBin').val('');

	  	$('#cMul').readonly="true";
	  	$('#aMulBin').readonly="true";
	  	$('#bMulBin').readonly="true";
	  	$('#cMulBin').readonly="true";

		$('#divMultiplicacion').show();
	}
}

function callDiv(){
	if( $('#divRadio').is(":checked") ){
		removeAll();

		$('#qDiv').readonly="false";
		$('#rDiv').readonly="false";
	  	/*$('#aDivBin').readonly="false";
	  	$('#dDivBin').readonly="false";
	  	$('#qDivBin').readonly="false";
	  	$('#rDivBin').readonly="false";*/
	  	
	  	$('#aDiv').val('');
	  	$('#dDiv').val('');
	  	$('#qDiv').val('');
	  	$('#rDiv').val('');
	  	/*$('#aDivBin').val('');
	  	$('#dDivBin').val('');
	  	$('#qDivBin').val('');
	  	$('#rDivBin').val('');*/

	  	$('#qDiv').readonly="true";
		$('#rDiv').readonly="true";
	  	/*$('#aDivBin').readonly="true";
	  	$('#dDivBin').readonly="true";
	  	$('#qDivBin').readonly="true";
	  	$('#rDivBin').readonly="true";*/

		$('#divDivicion').show();
	}
}

function callMod(){
	if( $('#modRadio').is(":checked") ){

		$('#bMod').val('');
	  	$('#expMod').val('');
	  	$('#mMod').val('');

		$('#expModBin').readonly="false"
	  	$('#mResultado').readonly="false"
	  	
	  	$('#expModBin').val( '' );
	  	$('#mResultado').val( '' );

	  	$('#expModBin').readonly="true"
	  	$('#mResultado').readonly="true"

		removeAll();
		$('#divExponencialModulo').show();
	}
}

function callExp(){
	if( $('#expRadio').is(":checked") ){
		removeAll();
		$('#divSuma').show();
	}
}

function removeAll(){
	$('.Operaciones').hide();
}