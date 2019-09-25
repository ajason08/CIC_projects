import it.uniroma1.lcl.babelfy.commons.BabelfyConfiguration;
import it.uniroma1.lcl.babelfy.commons.annotation.SemanticAnnotation;
import it.uniroma1.lcl.babelfy.core.Babelfy;
import it.uniroma1.lcl.jlt.util.Language;

import java.io.IOException;
import java.util.List;

public class running_babelfy {


    public static void main(String[] args) throws IOException {
  /*      BufferedWriter writer = Files.newBufferedWriter(Paths.get("hola"));
        writer.write("hola");
        writer.close();
*/
        Babelfy bfy = new Babelfy();
        BabelfyConfiguration bcc = BabelfyConfiguration.getInstance();
//        bcc.getMaxAmbiguityProperty();

        String inputText = "the Small Business Administration sixfold";
        List<SemanticAnnotation> bfyAnnotations = bfy.babelfy(inputText, Language.EN);



        //bfyAnnotations is the result of Babelfy.babelfy() call
        for (SemanticAnnotation annotation : bfyAnnotations)
        {

            String bnid = annotation.getBabelSynsetID();
            //splitting the input text using the CharOffsetFragment start and end anchors
            String frag = inputText.substring(annotation.getCharOffsetFragment().getStart(),
                    annotation.getCharOffsetFragment().getEnd() + 1);
            System.out.println(frag + "\t" + annotation.getBabelSynsetID());
            System.out.println("\t" + annotation.getBabelNetURL());
            System.out.println("\t" + annotation.getDBpediaURL());
            System.out.println("\t" + annotation.getSource());
        }

    }// end main


}