#!/usr/bin/env ruby
s = ARGV[0]

from = /from:([+]?\w*)/.match s
to = /to:([+]?\d*)/.match s
flags = /flags:((:?-?\d)+)/.match s
puts [from[1], to[1], flags[1]].join(',')
