# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import argparse
import utils

argp = argparse.ArgumentParser()
argp.add_argument('--eval_corpus_path',
    help="Path of the corpus to evaluate on", default=None)
args = argp.parse_args()

nlines = len(open(args.eval_corpus_path, encoding='utf-8').readlines())
predictions = ['London'] * nlines

total, correct = utils.evaluate_places(args.eval_corpus_path, predictions)
print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))
