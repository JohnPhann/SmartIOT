package com.example.aaa;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class LoginActivity extends AppCompatActivity {

        private EditText Name;
        private EditText Password;
        private TextView Info;
        private Button Login;
        int counter = 5;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        Name = (EditText)findViewById(R.id.editName);
        Password = (EditText)findViewById(R.id.editPassword);
        Info = (TextView)findViewById(R.id.info1);
        Login = (Button)findViewById(R.id.go);


        Info.setText("NO of attempts remaining : 5");
        Login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                validate(Name.getText().toString(),Password.getText().toString());
            }
        });
    }


    private void validate(String UserName , String UserPassowrd){
        if ((UserName.equals("admin")) && (UserPassowrd.equals("12345"))){
            Intent intent = new Intent(LoginActivity.this,UiActivity.class);
            startActivity(intent);
        }
        else{
            counter--;
            Info.setText("No of attempts remaining: "+String.valueOf(counter));
            if (counter == 0){
                Login.setEnabled(false);
            }
        }
    }
}
