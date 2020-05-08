import warnings
warnings.filterwarnings(action='ignore')

def main():
    import application as app
    app.run()

def clear_log():
    import logging
    import os
    import tensorflow as tf

    logger = logging.getLogger('chardet')
    logger.setLevel(logging.CRITICAL)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    tf.logging.set_verbosity(tf.logging.ERROR)

if __name__ == '__main__':
    #print('I\'m preparing for answering...')
    print('Provided Feature : 강의교수님', end='\n\n')
    clear_log()
    main()
