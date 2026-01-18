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
        private Logger logger;

        public Form1()
        {
            InitializeComponent();

            var ofd = new OpenFileDialog();
            ofd.Title = "Select NLog.config.";

            if (ofd.ShowDialog() == DialogResult.OK)
            {
                LogManager.Setup().LoadConfigurationFromFile(ofd.FileName);
                logger = LogManager.GetLogger("logA");

                logger.Trace("Trace (C#)");
                logger.Debug("Debug (C#)");
                logger.Info("Info (C#)");
                logger.Warn("Warn (C#)");
                logger.Error("Error (C#)");
                logger.Fatal("Fatal (C#)");


                MessageBox.Show("Finish.");
            }

            Environment.Exit(0);
        }
    }
}
