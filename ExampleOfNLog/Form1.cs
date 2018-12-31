using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using NLog;

namespace ExampleOfNLog
{
    public partial class Form1 : Form
    {
        private Logger logger = null;

        public Form1()
        {
            InitializeComponent();

            var ofd = new OpenFileDialog();

            if (ofd.ShowDialog() == DialogResult.OK)
            {
                LogManager.LoadConfiguration(ofd.FileName);
                logger = LogManager.GetLogger("logA");

                logger.Trace("Trace");
                logger.Debug("Debug");
                logger.Info("Info");
                logger.Warn("Warn");
                logger.Error("Error");
                logger.Fatal("Fatal");


                MessageBox.Show("Finish.");
            }

            Environment.Exit(0);
        }
    }
}
