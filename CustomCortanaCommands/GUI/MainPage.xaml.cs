using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using System.Threading.Tasks;
using Windows.ApplicationModel.Core;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.Storage;
using Windows.System;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;

// The Blank Page item template is documented at https://go.microsoft.com/fwlink/?LinkId=402352&clcid=0x409

namespace GUI
{
    /// <summary>
    /// An empty page that can be used on its own or navigated to within a Frame.
    /// </summary>
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
            this.InitializeComponent();
    }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            CoreApplication.Exit();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            runIt();
        }

        async void runIt()
        {
            // Path to the file in the app package to launch
            string imageFile = @"Assets\smarter.py";

            var file = await Windows.ApplicationModel.Package.Current.InstalledLocation.GetFileAsync(imageFile);

            if (file != null)
            {
               
            }
            else
            {
                // Could not find file
            }
        }
    }
}
