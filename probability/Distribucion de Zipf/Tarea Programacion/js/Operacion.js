
class Operacion {
    constructor() {}

    exeSuma(a, b){
        var maxLength = (a.length>b.length)?a.length : b.length;

        a = this.getCompletarLongitudBinario(a, maxLength);
        b = this.getCompletarLongitudBinario(b, maxLength);

        var s = this.addition(a,b);
        return s;
    }

    exeMul(a, b){
        a = this.getBinario(a);
        b = this.getBinario(b);

        var maxLength = (a.length>b.length)?a.length : b.length;

        a = this.getCompletarLongitudBinario(a, maxLength);
        b = this.getCompletarLongitudBinario(b, maxLength);

        var p = this.multiplication(a, b);
        return p;
    }

    exeDiv(a, d){
        var qr = this.divAndMod(a, d);
        return qr;
    }

    exeMod(b,exp,m){
        var x = this.modularExponentiation(b,exp,m);
        return x;
    }

    addition(a, b){
        var maxLength = (a.length>b.length)?a.length : b.length;
        //Algoritmo de suma------
        var s = String();
        var c = 0;
        for( var i=maxLength-1; i>=0; i--){
            var d = Math.floor( (parseInt(a.charAt(i))+parseInt(b.charAt(i))+c)/2 );
            s = (parseInt(a.charAt(i))+parseInt(b.charAt(i))+c-2*d) + s;
            c = d
        }
        s = c+s;
        return s;
        //------------------------
    }

    multiplication(a, b){
        var maxLength = (a.length>b.length)?a.length : b.length;
        //Algoritmo de Multiplicación------
        var c = new Array();
        var j=0;
        for( var i=maxLength-1; i>=0; i--){
            if( b.charAt(i)=='1' ){ c[j] = this.concatenarCeros(a,j); }
            else c[j] = '0';
            j++;
        }

        var p = String('0');
        for( var j=0; j<c.length; j++){
            p = this.exeSuma(p, c[j]);
        }
        return p;
        //--------------------------------
    }

    divAndMod(a, d){
        //Algoritmo de Divición y modulo --------------
        var q = 0;
        var r = Math.abs(a);

        while( r>=d ){
            r = r-d;
            q = q+1;
        }

        if(a<0 && r>0){ 
            r = d-r;
            q = -1*(q+1); 
        }

        var qr = new Array();
        qr[0] = q;
        qr[1] = r;

        return qr 
        //----------------------------------------------
    }

    modularExponentiation(b,exp,m){
        //Algoritmo "modular exponencial" --------------
        var x = 1;
        var power = b%m;
        for( var i=exp.length-1; i>=0; i-- ){
            if( exp.charAt(i)==1 ){ x=(x*power)%m; }
            power = (power*power)%m;
        }
        return x;
        //-----------------------------------------------
    }

    //Metodo para obtener el binario
    getBinario( number) {
        var base = 2;
        return Number(number).toString(base);
    };

    //Metodo para rellenar con 0
    getCompletarLongitudBinario(valA, maxLength) {
        while(valA.length<maxLength){ valA = '0'+valA; }
        return valA;
    };

    concatenarCeros(a, j){
        for(var i=0; i<j; i++){ a = a+'0'; }
        return a;
    }

    getMedia(a,b){
        if(a.length==1 || b.length==1 ){
            var maxA = Math.max.apply(null, a);
            var maxB = Math.max.apply(null, b);
            var mediana = Math.max(maxA,maxB);
            return mediana;
        }
        var m = Math.ceil(b.length/2);

        var a2= new Array();
        var b2= new Array();
        if(b[m]>a[m]){
            for(var i=0;i<m;i++){
                b2[i] = b[i];// -
            }
            var j=0;
            for(var i=m-1;i<a.length;i++){
                a2[j] = a[i];// +
                j++;
            }
        }
        else{
            for(var i =0;i<m;i++){
                a2[i] = a[i];// -
            }
            j=0;
            for(var i=m-1;i<b.length;i++){
                b2[j] = b[i];// +
                j++;
            } 
        }
        this.getMedia(a2,b2);
    }
}

