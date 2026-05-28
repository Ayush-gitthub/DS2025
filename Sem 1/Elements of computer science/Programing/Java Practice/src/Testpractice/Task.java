package Testpractice;

import java.util.*;

public class Task {
    private HashMap<Integer, Item> x = new HashMap<>();
    public Task(Collection<Item> items)
    {
        for(Item item : items)
        {
            if(x.containsKey(item.getId()))
            {
                throw new IllegalArgumentException("Key Exists");
            }
            x.put(item.getId(), item);
        }
    }
    public void addItem(Item item)
    {
        if(x.containsKey(item.getId()))
        {
            throw new IllegalArgumentException("Key Exists");
        }
        x.put(item.getId(), item);
    }
    public void applyDiscount(String category, double percent)
    {
        if(percent<0 || percent>100)
            return ;
        for(Item item : x.values())
        {
            if(item.getCategory().equals(category))
            {
                double price = item.getPrice();
                price = price - ((percent*price)/100.0);
                item.setPrice(price);
            }
        }
    }
    public Map<String, List<Item>> getCategoryMap(){
        Map<String, List<Item>> y = new HashMap<>();
        for(Item item : x.values())
        {
            if(y.containsKey(item.getName()))
            {
                y.get(item.getName()).add(item);
            }
            else {
                ArrayList<Item> temp = new ArrayList<>();
                temp.add(item);
                y.put(item.getName(), temp);
            }
        }
        return y;
    }
    public Collection<Item> getItemsUnder(double maxPrice)
    {
        Collection<Item> y = new ArrayList<Item>();
        for(Item item : x.values())
        {
            if(item.getPrice()<maxPrice)
                y.add(item);
        }
        return y;
    }

    @Override
    public String toString() {
        return x.values().toString();
    }

    public static void main(String[] args){
        Item i1 = new Item(1, "Apple",  "Fruit",  1.20);
        Item i2 = new Item(2, "Banana", "Fruit",  0.80);
        Item i3 = new Item(3, "Milk",   "Dairy",  0.99);
        Task t = new Task(List.of(i1, i2, i3));
        System.out.println(t);
        t.applyDiscount("Fruit", 50);
        System.out.println(t);
        System.out.println(t.getCategoryMap());
        System.out.println(t.getItemsUnder(1.0));
//        assert t.getCategoryMap().get("Fruit").get(0).price == 0.40; // Banana after 50% off
//        assert t.getItemsUnder(1.0).size() == 3; // all under 1.0 after discount
//// duplicate id:
//        try { t.addItem(new Item(1,"X","Y",1.0)); assert false; }
//        catch (IllegalArgumentException e) { }

    }

}
