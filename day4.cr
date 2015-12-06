require "crypto/md5"

start = File.read("input/04").chomp '\n'
counter = 0
hashed = ""
until hashed.starts_with? "000000"
  counter += 1
  hashed = Crypto::MD5.hex_digest(start + counter.to_s)
end
p "Solution: #{counter} MD5: #{hashed}"
