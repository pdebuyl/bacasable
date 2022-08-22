
all: hello

clean:
	rm -f hello
.PHONY: clean

hello: hello.c
	$(CC) -Wall -std=c99 -o $@ $<
