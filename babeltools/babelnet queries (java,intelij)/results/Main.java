//import it.uniroma1.lcl.babelnet.BabelNet;

import com.babelscape.util.UniversalPOS;
import it.uniroma1.lcl.babelnet.*;
import it.uniroma1.lcl.babelnet.data.BabelPointer;
import it.uniroma1.lcl.babelnet.data.BabelSenseSource;
import it.uniroma1.lcl.jlt.util.Language;

import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Collectors;


public class Main {

    private static Map create_dict(){
        Map<String, Integer> map = new HashMap<String, Integer>();
        /* // in case you want to change the order
        map.put("hypernym", 0);
        map.put("semantically_related_form", 0);
        map.put("parent_taxon", 0);
        map.put("taxon_rank", 0);
        map.put("native_language", 0);
        map.put("position_held", 0);
        map.put("place_of_death", 0);
        map.put("place_of_birth", 0);
        map.put("country", 0);
        map.put("located_in_the_administrative_territorial_entity", 0);
        */
        map.put("hypernym", 0);
        map.put("semantically_related_form", 1);
        map.put("parent_taxon", 2);
        map.put("taxon_rank", 3);
        map.put("native_language", 4);
        map.put("position_held", 5);
        map.put("place_of_death", 6);
        map.put("place_of_birth", 7);
        map.put("country", 8);
        map.put("located_in_the_administrative_territorial_entity", 9);

        return map;
    }

    private static void get_vertex_info(String outPath) throws IOException {
        int num_nodes = 15780364; // I knew from variable inspector of iterator

        BabelNet bn = BabelNet.getInstance();
        Iterator<BabelSynset> synsetIterator = bn.iterator();
        int counter = 0; int stop = 100;
        BufferedWriter writer = Files.newBufferedWriter(Paths.get(outPath));

        //while (synsetIterator.hasNext() && counter<stop) {
        while (synsetIterator.hasNext()) {
            //BabelSynset next = synsetIterator.next();
            writer.write(synsetIterator.next().getID() + "\n");
            counter += 1; System.out.println(counter +"\t" +100*(float)counter/num_nodes);

        }
        writer.close();
    }
    private static void buildBNGraph(String outPath) throws IOException {
        int num_nodes = 15780364; // I knew from variable inspector of iterator
        Map<String, Integer> my_map = new HashMap<String, Integer>();

        BabelNet bn = BabelNet.getInstance();
        Iterator<BabelSynset> synsetIterator = bn.iterator();
        int counter = 0; int stop = 100;
        BufferedWriter writer = Files.newBufferedWriter(Paths.get(outPath));

        BufferedWriter log = Files.newBufferedWriter(Paths.get(outPath+"_log"));
        int rel_id=0;

        while (synsetIterator.hasNext() && counter<stop) {
        //while (synsetIterator.hasNext()) {
            BabelSynset next = synsetIterator.next();

            for (BabelSynsetRelation edge : next.getOutgoingEdges()) {
            //for (BabelSynsetRelation edge : next.getOutgoingEdges(BabelPointer.SEMANTICALLY_RELATED, BabelPointer.ANY_HYPERNYM, BabelPointer.ANY_HOLONYM)) {
                //if(edge.getLanguage() == Language.EN){

                if (my_map.get(edge.getPointer().toString()) ==null){
                    System.out.println(edge.getPointer().toString());
                    log.write(rel_id+ "\t"
                            + edge.getPointer().toString()+ "\t"
                            + edge.getPointer().getShortName()+ "\t"
                            + edge.getPointer().getName()+ "\t"
                            + edge.getPointer().getRelationGroup()+ "\t"
                            + edge.getPointer().hashCode()+ "\t"
                            + edge.getPointer().getSymbol()+ "\t"
                            + edge.getPointer().isAutomatic()
                            +"\n"
                    );

                    my_map.put(edge.getPointer().toString(),rel_id);
                    rel_id +=1;
                }

                writer.write( counter + " "
                        + next.getID() + " "
                        + edge.getBabelSynsetIDTarget()+ " "
                        + my_map.get(edge.getPointer().toString())
                        + "\n"
                );
            }
            counter += 1; System.out.println(counter +"\t" +100*(float)counter/num_nodes);
        }
        writer.close();
        log.close();
    }




    // graph with bn and replacing n for 1+code
    private static void buildBNGraph2(String outPath) throws IOException {
        int num_nodes = 15780364; // I knew from variable inspector of iterator
        Map<String, Integer> my_map = new HashMap<String, Integer>();

        BabelNet bn = BabelNet.getInstance();
        Iterator<BabelSynset> synsetIterator = bn.iterator();
        int counter = 0; int stop = 100;
        BufferedWriter writer = Files.newBufferedWriter(Paths.get(outPath));

        BufferedWriter log = Files.newBufferedWriter(Paths.get(outPath+"_log"));
        //BufferedWriter aux = Files.newBufferedWriter(Paths.get(outPath+"_aux"));

        int sufix_id=1;

        //while (synsetIterator.hasNext() && counter<stop) {
        while (synsetIterator.hasNext()) {
            BabelSynset next = synsetIterator.next();

            for (BabelSynsetRelation edge : next.getOutgoingEdges()) {
                //for (BabelSynsetRelation edge : next.getOutgoingEdges(BabelPointer.SEMANTICALLY_RELATED, BabelPointer.ANY_HYPERNYM, BabelPointer.ANY_HOLONYM)) {
                //if(edge.getLanguage() == Language.EN){
                String id = next.getID().toString();
                String target = edge.getBabelSynsetIDTarget().toString();

                // transformation from bn:01110435n to 1+1110435, trim left 0 and adding POS code
                // instead of hashing in order to preserve the bn code
                // currently im loosing the relations, but I can retrive them using node codes.
                int id_base = Integer.parseInt(id.substring(3,id.length() - 1));
                int target_base = Integer.parseInt(target.substring(3,target.length() - 1));


                String id_char= id.substring(id.length() - 1);
                String target_char= target.substring(target.length() - 1);

                if (my_map.get(id_char) ==null){
                    my_map.put(id_char,sufix_id);
                    sufix_id +=1;
                    log.write(id_char+ "\n");
                }

                if (my_map.get(target_char) ==null){
                    my_map.put(target_char,sufix_id);
                    sufix_id +=1;
                    log.write(target_char+ "\n");
                }
                id = my_map.get(id_char).toString()+String.valueOf(id_base);
                target = my_map.get(target_char).toString()+String.valueOf(target_base);


/*                if (my_map.get(edge.getPointer().toString()) ==null){
                    System.out.println(edge.getPointer().toString());
                    log.write(rel_id+ "\t"
                            + edge.getPointer().toString()+ "\t"
                            + edge.getPointer().getShortName()+ "\t"
                            + edge.getPointer().getName()+ "\t"
                            + edge.getPointer().getRelationGroup()+ "\t"
                            + edge.getPointer().hashCode()+ "\t"
                            + edge.getPointer().getSymbol()+ "\t"
                            + edge.getPointer().isAutomatic()
                            +"\n"
                    );

                    my_map.put(edge.getPointer().toString(),rel_id);
                    rel_id +=1;
                }
*/
                writer.write(id + " "
                        + target+ " "
                //        + my_map.get(edge.getPointer().toString())
                        + "\n"
                );
                /*
                aux.write(id + " "
                        + target+ " "
                        + my_map.get(edge.getPointer().toString())
                        + "\n"
                );

*/
            }
            counter += 1;

            System.out.println(counter +"\t" +100*(float)counter/num_nodes);
        }
        writer.close();
        log.close();
    }

    // as edge list as: node -[set of neiborg$short_name]
    private static void buildBNGraph3(String outPath) throws IOException {
        int num_nodes = 15780364; // I knew from variable inspector of iterator
        //Map<String, String> my_map = new HashMap<String, String>();

        BabelNet bn = BabelNet.getInstance();
        Iterator<BabelSynset> synsetIterator = bn.iterator();
        int counter = 0; int stop = 100;
        BufferedWriter writer = Files.newBufferedWriter(Paths.get(outPath));

        //BufferedWriter log = Files.newBufferedWriter(Paths.get(outPath+"_log"));
        int rel_id=0;

        //while (synsetIterator.hasNext() && counter<stop) {
        while (synsetIterator.hasNext()) {
            BabelSynset next = synsetIterator.next();

            writer.write(next.getID() + "\t");
            for (BabelSynsetRelation edge : next.getOutgoingEdges()) {
                //for (BabelSynsetRelation edge : next.getOutgoingEdges(BabelPointer.SEMANTICALLY_RELATED, BabelPointer.ANY_HYPERNYM, BabelPointer.ANY_HOLONYM)) {
                //if(edge.getLanguage() == Language.EN){
/*
                if (my_map.get(edge.getPointer().getShortName()) ==null){
                    System.out.println(edge.getPointer().getShortName());

                    log.write(rel_id+ "\t"
                            + edge.getPointer().toString()+ "\t"
                            + edge.getPointer().getShortName()+ "\t"
                            + edge.getPointer().getName()+ "\t"
                            + edge.getPointer().getRelationGroup()+ "\t"
                            + edge.getPointer().hashCode()+ "\t"
                            + edge.getPointer().getSymbol()+ "\t"
                            + edge.getPointer().isAutomatic()
                            +"\n"
                    );


                    my_map.put(edge.getPointer().getShortName(),rel_id);
                    rel_id +=1;
                }*/

                writer.write( edge.getBabelSynsetIDTarget()+ "$"+ edge.getPointer().getShortName()+" ");
            }
            writer.write("\n");
            counter += 1; System.out.println(counter +"\t" +100*(float)counter/num_nodes);
        }
        writer.close();
        //log.close();
    }

    private static void buildBNGraph5(String outPath) throws IOException {
        int num_nodes = 15780364; // I knew from variable inspector of iterator
        Map<String, Integer> my_map = new HashMap<String, Integer>();
        Map<String, Integer> my_counts = new HashMap<String, Integer>();

        BabelNet bn = BabelNet.getInstance();
        Iterator<BabelSynset> synsetIterator = bn.iterator();
        int counter = 0; int stop = 100;
        BufferedWriter writer = Files.newBufferedWriter(Paths.get(outPath));

        BufferedWriter log = Files.newBufferedWriter(Paths.get(outPath+"_log"));
        BufferedWriter log_frequencies = Files.newBufferedWriter(Paths.get(outPath+"_log_freq"));
        int rel_id=0;

        //while (synsetIterator.hasNext() && counter<stop) {
            while (synsetIterator.hasNext()) {
            BabelSynset next = synsetIterator.next();

            for (BabelSynsetRelation edge : next.getOutgoingEdges()) {
                //for (BabelSynsetRelation edge : next.getOutgoingEdges(BabelPointer.SEMANTICALLY_RELATED, BabelPointer.ANY_HYPERNYM, BabelPointer.ANY_HOLONYM)) {
                //if(edge.getLanguage() == Language.EN){
                Integer rel_in_map = my_map.get(edge.getPointer().toString());

                if (rel_in_map ==null){
                    System.out.println(edge.getPointer().toString());
                    log.write(rel_id+ "\t"
                            + edge.getPointer().toString()+ "\t"
                            + edge.getPointer().getShortName()+ "\t"
                            + edge.getPointer().getName()+ "\t"
                            + edge.getPointer().getRelationGroup()+ "\t"
                            + edge.getPointer().hashCode()+ "\t"
                            + edge.getPointer().getSymbol()+ "\t"
                            + edge.getPointer().isAutomatic()
                            +"\n"
                    );
                    my_map.put(edge.getPointer().toString(),rel_id);
                    my_counts.put(edge.getPointer().toString(),1);
                    rel_id +=1;

                }
                else{
                    Integer current_count = my_counts.get(edge.getPointer().toString());
                    my_counts.put(edge.getPointer().toString(),current_count+1);
                }

                writer.write( counter + " "
                        + next.getID() + " "
                        + edge.getBabelSynsetIDTarget()+ " "
                        + my_map.get(edge.getPointer().toString())
                        + "\n"
                );
            }
            counter += 1; System.out.println(counter +"\t" +100*(float)counter/num_nodes);
        }
        log_frequencies.write(my_counts.toString());
        writer.close();
        log.close();
        log_frequencies.close();

    }

    private static void listedges(String babel_id){
        BabelNet bn = BabelNet.getInstance();
        BabelSynset by = bn.getSynset(new BabelSynsetID(babel_id));

        for (BabelSynsetRelation edge : by.getOutgoingEdges()) {
            //for (BabelSynsetRelation edge : next.getOutgoingEdges(BabelPointer.SEMANTICALLY_RELATED, BabelPointer.ANY_HYPERNYM, BabelPointer.ANY_HOLONYM)) {
            //if(edge.getLanguage() == Language.EN){
            String target = edge.getBabelSynsetIDTarget().toString();

            System.out.println(target+ "\t"
                    + edge.getPointer().toString()+ "\t"
                    + edge.getPointer().getShortName()+ "\t"
                    + edge.getPointer().getName()+ "\t"
                    + edge.getPointer().getRelationGroup()+ "\t"
                    //+ edge.getPointer().hashCode()+ "\t"
                    //+ edge.getPointer().getSymbol()+ "\t"
                    //+ edge.getPointer().isAutomatic()
            );
        }
    }

    // id_neo id_babel target short_name_relation
    private static void buildBNGraph4(String outPath) throws IOException {
        int num_nodes = 15780364; // I knew from variable inspector of iterator
        String shortname = ""; String related_alias = "wiki";

        BabelNet bn = BabelNet.getInstance();
        Iterator<BabelSynset> synsetIterator = bn.iterator();
        int counter = 0; int stop = 10000;
        BufferedWriter writer = Files.newBufferedWriter(Paths.get(outPath));
        writer.write("id target rela\n");


        //while (synsetIterator.hasNext() && counter<stop) {
        while (synsetIterator.hasNext()) {
            BabelSynset next = synsetIterator.next();

            for (BabelSynsetRelation edge : next.getOutgoingEdges()) {
                //for (BabelSynsetRelation edge : next.getOutgoingEdges(BabelPointer.SEMANTICALLY_RELATED, BabelPointer.ANY_HYPERNYM, BabelPointer.ANY_HOLONYM)) {
                //if(edge.getLanguage() == Language.EN){
                if (edge.getBabelSynsetIDTarget().toString().equalsIgnoreCase(next.getID().toString())){
                    //System.out.println(next.getID());
                    //System.out.println(edge.getBabelSynsetIDTarget());
                    continue;
                }
                shortname =edge.getPointer().getShortName();
                if (shortname.equalsIgnoreCase("related")){
                    shortname = related_alias;
                }
                else if(!edge.getPointer().getRelationGroup().toString().equalsIgnoreCase("OTHER")){
                    shortname = edge.getPointer().getRelationGroup().toString().toLowerCase();
                    //System.out.println(shortname);
                }
                else{
                    shortname = shortname.replaceAll("[()'/]", "").replaceAll("[-]", "_");
                }

                writer.write( next.getID() + " "
                        + edge.getBabelSynsetIDTarget()+ " "
                        + shortname
                        + "\n"
                );
            }
            counter += 1; System.out.println(counter +"\t" +100*(float)counter/num_nodes);
        }
        writer.close();
    }
    private static void from_wordnet_to_babelnet(String inPath) throws IOException {
        BabelNet bn = BabelNet.getInstance();
        BabelSynset by1, by2;
        BufferedWriter writer = Files.newBufferedWriter(Paths.get(inPath+"_out"));
        int counter = 0;

        List<String> a = Files.lines(Paths.get(inPath)).collect(Collectors.toList());
        for(String line: a){

            String part1 = line.split(" ")[0];
            String part2 = line.split(" ")[1];
            by1 = bn.getSynset(new WordNetSynsetID("wn:"+part1));
            by2 = bn.getSynset(new WordNetSynsetID("wn:"+part2));

            writer.write(by1.getID().toString()+" "+by2.getID().toString());
            writer.write("\n");
            counter++;
        }
        writer.close();


    }
    private static String big_neighborg(String node) throws IOException {
        BabelNet bn = BabelNet.getInstance();
        BabelSynset by = bn.getSynset(new BabelSynsetID(node));
        String big = "";
        int max = 0;
        int counter = 0;
        //List<BabelSynsetRelation> edges =by.getOutgoingEdges(BabelPointer.ANY_HYPERNYM, BabelPointer.ANY_HOLONYM);
        List<BabelSynsetRelation> edges =by.getOutgoingEdges(BabelPointer.ANY_MERONYM);
        for (BabelSynsetRelation edge : edges) {

            String target_id = edge.getBabelSynsetIDTarget().toString();
            BabelSynset target = bn.getSynset(new BabelSynsetID(target_id));
            int neighborg_neighborgs =target.getOutgoingEdges().size();
            if (neighborg_neighborgs>max){
                big = target_id;
                max = neighborg_neighborgs;
            }
            System.out.println(counter + " of "+ edges.size());
            counter+=1;
        }
        System.out.println(big + "_"+ max);
        return big;
    }
    private static void any_sand_box(/*String outPath*/) throws IOException {
        BabelNet bn = BabelNet.getInstance();
  /*      BabelSynset by = bn.getSynset(new WordNetSynsetID("wn:06879521n"));
        // Most relevant BabelSense to this BabelSynset for a given language.
        Optional<BabelSense> bs = by.getMainSense(Language.EN);
        System.out.println(by.getSenses(Language.EN));

// Gets the part of speech of this BabelSynset.
        POS pos = by.getPOS();
// True if the BabelSynset is a key concept
        boolean iskeyConcept = by.isKeyConcept();
// Gets the senses contained in this BabelSynset.
        List<BabelSense> senses = by.getSenses();
// Collects all BabelGlosses in the given source for this BabelSynset.
        List<BabelGloss> glosses = by.getGlosses();
// Collects all BabelExamples for this BabelSynset.
        List<BabelExample> examples = by.getExamples();
// Gets the images (BabelImages) of this BabelSynset.
        List<BabelImage> images = by.getImages();
// Collects all the edges incident on this BabelSynset.
        List<BabelSynsetRelation> edges = by.getOutgoingEdges();
// Gets the BabelCategory objects of this BabelSynset.
        List<BabelCategory> cats = by.getCategories();

        System.out.println(pos);
        System.out.println(bs);
        System.out.println(iskeyConcept);
        System.out.println(senses);
        System.out.println(glosses);
        System.out.println(examples);
        System.out.println(images);
        //System.out.println(edges);
        System.out.println(cats);
        System.out.println("-------------------------------");
*/
        BabelNetQuery query = new BabelNetQuery.Builder("scene")
                .from(Language.EN)
                .POS(UniversalPOS.NOUN)
                .sources(Arrays.asList(BabelSenseSource.WN))
                .build();
        List<BabelSense> senses2 = bn.getSensesFrom(query);
        for (BabelSense ws : senses2){
            System.out.println(ws.getSynset() + " "+ws.getSynsetID() + " "+ ws.getSynset().getSenses() + " " + ws.getSimpleLemma());
        }

        //System.out.println(senses2);
/*
        BabelNet bn = BabelNet.getInstance();
        BabelSynset by = bn.getSynset(new BabelSynsetID("bn:00082705v"));
        System.out.println(by.getType().name());
        System.out.println(by.getID());
        List<BabelSense> wn_senses = by.getSenses(Language.EN, BabelSenseSource.WN);
        for (BabelSense ws : wn_senses){
            System.out.println(ws.getFullLemma() + " " + ws.getSimpleLemma());
        }
        */
    }
    public static void main(String[] args) throws IOException {
        String my_path= "/home/jason/my_temp/";
        String my_path2= "/home/jason/bin/neo4j-community-3.4.10/import/";
        //buildBNGraph(my_path+"babel_outputx2");
        //buildBNGraph2(my_path);
        //buildBNGraph3(my_path+"babel_outputN2");
        //buildBNGraph4(my_path+"babel_outputx2");
        buildBNGraph5(my_path+"babel_outputF");
        //listedges("bn:03323142n");
        //get_vertex_info(my_path+"babel_nodes");
        //from_wordnet_to_babelnet("/home/jason/Downloads/arcs_test_maru_9707.txt");
        //big_neighborg("bn:00069636n");
        //any_sand_box();




    }// end main
}
