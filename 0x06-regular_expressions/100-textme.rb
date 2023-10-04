#!/usr/bin/env ruby
SENDER = ARGV[0].scan(/from:(?:[[:alpha:]]+|\+?[0-9]{11})/).join.gsub('from:', '')
RECEIVER = ARGV[0].scan(/to:(?:[A-za-z]+|\+?[0-9]{11})/).join.gsub('to:', '')
FLAGS = ARGV[0].scan(/flags:(?:\-?[(0-1)]:?){5}/).join.gsub('flags:', '')

s = SENDER.empty? ? 'N/A' : SENDER
r = RECEIVER.empty? ? 'N/A' : RECEIVER
f = FLAGS.empty? ? 'N/A' : FLAGS

puts "#{s}, #{r}, #{f}"
