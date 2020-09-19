package com.example.aaa;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.view.View;
import android.view.View.OnClickListener;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.MediaController;
import android.widget.Toast;
import android.widget.VideoView;
import android.net.Uri;
import android.os.Bundle;
import android.content.Intent;
import android.view.KeyEvent;
import android.view.WindowManager;

import com.example.aaa.R;

public class MainActivity extends AppCompatActivity {

    EditText addrField;
    Button btnConnect;
    //VideoView streamView;
    WebView webView;
    private String WebView;
    //private String s = "http://192.168.2.210:5000";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        addrField = (EditText)findViewById(R.id.addr);
        btnConnect = (Button)findViewById(R.id.connect);
        //streamView = (VideoView)findViewById(R.id.streamview);

        btnConnect.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                String s = addrField.getEditableText().toString();
                //playStream(s);

                setContentView(R.layout.web);
                webView = (WebView)findViewById(R.id.web_view);

                //JavaScriptを有効化
                webView.getSettings().setJavaScriptEnabled(true);

                //Web Strageを有効化
                webView.getSettings().setDomStorageEnabled(true);

                //Hardware Acceleration ON
                getWindow().setFlags(
                        WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED,
                        WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED);

                webView.loadUrl(s);
            }
        });


    }

    /*private void playStream(String src){
        Uri UriSrc = Uri.parse(src);
        if(UriSrc == null){
            Toast.makeText(MainActivity.this,
                    "UriSrc == null", Toast.LENGTH_LONG).show();
        }else{
            streamView.setVideoURI(UriSrc);
            mediaController = new MediaController(this);
            streamView.setMediaController(mediaController);
            streamView.start();

            Toast.makeText(MainActivity.this,
                    "Connect: " + src,
                    Toast.LENGTH_LONG).show();
        }
    }*/

    /*@Override
    protected void onDestroy() {
        super.onDestroy();
        webView.stopPlayback();
    }*/




}