BINDIR=/usr/local/bin

all:
	make -C brutils all

clean:
	make -C brutils clean

install: all
	make -C brutils install
	install -c br $(BINDIR)

uninstall:
	make -C brutils uninstall
	rm $(BINDIR)/br
