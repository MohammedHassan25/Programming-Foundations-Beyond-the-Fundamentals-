# ---------------------------------------------------------------------------
# Input/Output is (I/O) for short.
# Input can take many different forms depending on the program.
# When the program has done what you requested that final result is output.
# ---------------------------------------------------------------------------

# for example

infile = open('values.txt', 'rt')
outfile = open('values-totaled.txt', 'wt')
print('processing input')
sum = 0
for line in infile:
    sum += int(line)
    print(line.rstrip(), file=outfile)
print('\nTotal: ' + str(sum), file=outfile)
outfile.close()
print('Output complete')
