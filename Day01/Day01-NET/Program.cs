using System.Linq;

class Day01 {
    public static string readInput() {
        try {
            using (var sr = new StreamReader("input.txt")) {
                return sr.ReadToEnd().Trim();
            }
        } catch (IOException) {
            Console.WriteLine("File could not be read.");
            return null;
        }
    }

    public static void partOne() {
        string text = readInput();
        string[] lines = text.Split('\n');

        int sum = 0;

        foreach (var line in lines) {
            string number = "";
            foreach (var c in line) {
                if (Char.IsDigit(c)) {
                    number += c;
                }
            }
            sum += int.Parse(number[0].ToString() + number[number.Length-1].ToString());
        }
        Console.WriteLine(sum);
    }

    public static List<int> findAll(string str, string query) {
        List<int> answer = new List<int>();
        for (int i = 0; i < str.Length - query.Length + 1; i++) {
            if (str[i..].StartsWith(query)) {
                answer.Add(i);
            }
        }
        return answer;
    }

    public static void partTwo() {
        var numbers = new Dictionary<string, string>() {
            {"one", "1"},
            {"two", "2"},
            {"three", "3"},
            {"four", "4"},
            {"five", "5"},
            {"six", "6"},
            {"seven", "7"},
            {"eight", "8"},
            {"nine", "9"}
        };

        string text = readInput();
        string[] lines = text.Split('\n');
        string[] values = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
        int sum = 0;

        foreach (var line in lines) {
            int minIndex = int.MaxValue;
            string min = "";
            int maxIndex = int.MinValue;
            string max = "";
            foreach (var val in values) {
                if (line.Contains(val)) {
                    var indices = findAll(line, val);
                    foreach (var index in indices) {
                        if (index > -1 && index < minIndex) {
                            minIndex = index;
                            if (Char.IsDigit(val, 0)) {
                                min = val;
                            } else {
                                min = numbers[val];
                            }
                        }
                        if (index > -1 && index > maxIndex) {
                            maxIndex = index;
                            if (Char.IsDigit(val, 0)) {
                                max = val;
                            } else {
                                max = numbers[val];
                            }
                        }
                    }
                }
            }
            string total = min + max;
            sum += int.Parse(total);
        }
        Console.WriteLine(sum);
    }

    static void Main(string[] args) {
        partOne();
        partTwo();
    }
}
