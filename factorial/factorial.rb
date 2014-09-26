##Calculates factorial for positive numbers; does not handle negative inputs.

def factorial x
    out = 1
    (1..x).each do|n|
        out *= n
    end
  out
end


if __FILE__ == $0
    (1..20).each do |n|
        print n, ": ", factorial(n)
        puts
    end
end