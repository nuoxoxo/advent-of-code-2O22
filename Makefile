#comp	:=	c++ -std=c++11 -Wall -Werror -Wextra
comp	:=	c++ -std=c++17
name	:=	out
rmv	:=	rm -f

pre	:=	_inputs/
src	:=	aoc2201.cc
src	:=	aoc2202a.cc
src	:=	aoc2202.cc
src	:=	aoc2203a.cc
src	:=	aoc2203.cc
src	:=	aoc2204a.cc
src	:=	aoc2204.cc
src	:=	aoc2205a.cc
src	:=	aoc2205.cc
src	:=	aoc2205_part1.cc
src	:=	aoc2205_part2.cc
src	:=	aoc2206.cc
src	:=	aoc2207a.cc
src	:=	aoc2207.cc
src	:=	aoc2208a.cc
src	:=	aoc2208.cc
src	:=	aoc2209.cc
src	:=	aoc2210.cc
src	:=	aoc2211.cc
# src	:=	different_solutions/aoc2212_s_to_e.cc
src	:=	aoc2212.cc
src	:=	aoc2215.cc
src	:=	aoc2216.cc
src	:=	aoc2219.cc
src	:=	aoc2222.cc

all	:	$(name)

$(name)	:	$(src)
		@ $(comp) $^ -o $@
		@ echo "data" && echo "" 
		@ ./$(name) < $(pre)2222.0
		@#@ ./$(name) < $(pre)2220.0
		@#@ ./$(name) < 2219.0
		@#@ ./$(name) < 2216.0
		@#@ ./$(name) < 2215.0
		@#@ ./$(name) < 2212.0
		@#@ ./$(name) < 2211.0
		@#@ ./$(name) < 2210.0
		@#@ ./$(name) < 2209.0
		@#@ ./$(name) < 2208.0
		@#@ ./$(name) < 2207.0
		@#@ ./$(name) < 2206.0
		@#@ ./$(name) < 2205.0
		@#@ ./$(name) < 2204.0
		@#@ ./$(name) < 2204a.0
		@#@ ./$(name) < 2203.0
		@#@ ./$(name) < 2203a.0
		@#@ ./$(name) < 2202.0
		@#@ ./$(name) < 2202a.0
		@#@ ./$(name) < 2201.0
		@#@ ./$(name) < 2209.1
		@ echo "" && echo "test" && echo ""
		@#@ ./$(name) < $(pre)2222.1
		@#@ ./$(name) < $(pre)2220.1
		@#@ ./$(name) < 2219.1
		@#@ ./$(name) < 2212.1
		@#@ echo "" && echo "test \n(part 2)" && echo ""
		@#@ ./$(name) < 2209.2
		@#@ ./$(name) < test
		@ make f

clean	:
		@ $(rmv) $(name)

fclean	:	clean
		@ $(rmv) out *.out

f	:	fclean
re	:	f all
.PHONY	:	fclean clean all re f
