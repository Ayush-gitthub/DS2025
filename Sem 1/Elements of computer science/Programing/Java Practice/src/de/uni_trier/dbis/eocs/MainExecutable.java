package de.uni_trier.dbis.eocs;
import optimizers.address.AddressOptimizer;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;
public class MainExecutable {

    public static void main(String[] args) {
        String fileName = "addresses.txt";
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = reader.readLine()) != null) {
                AddressOptimizer ao = new AddressOptimizer(line);

                List<String> result = ao.optimize();

                if (result == null || result.isEmpty()) {
                    System.out.println("empty result");
                } else {
                    for (String part : result) {
                        System.out.println(part);
                    }
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
    }
}

